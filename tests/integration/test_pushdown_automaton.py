import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', './api')))
from main import app 

client = TestClient(app)

pushdown_automaton_data = {
    "name": "pda1",
    "states": ['q0', 'q1', 'q2', 'q3'],
    "input_symbols": ['a', 'b'], 
    "stack_symbols": ['0', '1'], 
    "transitions": {
        'q0': {
            'a': {'0': ('q1', ('1', '0'))}
        },
        'q1': {
            'a': {'1': ('q1', ('1', '1'))},  
            'b': {'1': ('q2', '')}
        },
        'q2': {
            'b': {'1': ('q2', '')},
            '': {'0': ('q3', ('0',))} 
        }
    },
    "initial_state": 'q0',
    "initial_stack_symbol": '0',
    "final_states": ['q3'],
    "acceptance_mode": 'final_state'
}

def test_create_pda():
    response = client.post("/pushdown_automaton/", json=pushdown_automaton_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Pushdown Automaton created successfully!"}

def test_test_pda_accepted():
    response = client.get("/pushdown_automaton/pda1/test?input_string=ab")
    assert response.status_code == 200
    assert response.json() == {"accepted": True}

def test_test_pda_rejected():
    response = client.get("/pushdown_automaton/pda1/test?input_string=a")
    assert response.status_code == 200
    assert response.json() == {"accepted": False}

def test_test_pda_not_found():
    response = client.get("/pushdown_automaton/non_existent_pda/test?input_string=0101")
    assert response.status_code == 404
    assert response.json()['detail'] == {"error": "Automaton not found"}
