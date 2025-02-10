import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', './api')))
from main import app 

client = TestClient(app)

pushdown_automaton_data = {
    "name": "pushdown_automaton_1",
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

def test_create_pushdown_automaton():
    response = client.post("/pushdown_automaton/", json=pushdown_automaton_data)

    assert response.status_code == 200
    assert response.json() == {"message": "Pushdown Automaton created successfully!"}

def test_test_pushdown_automaton_accepted():
    client.post("/pushdown_automaton/", json=pushdown_automaton_data)

    response = client.get("/pushdown_automaton/pushdown_automaton_1/test?input_string=ab")

    assert response.status_code == 200
    assert response.json() == {"accepted": True}

def test_test_pushdown_automaton_rejected():
    client.post("/pushdown_automaton/", json=pushdown_automaton_data)

    response = client.get("/pushdown_automaton/pushdown_automaton_1/test?input_string=a")

    assert response.status_code == 200
    assert response.json() == {"accepted": False}

def test_test_pushdown_automaton_not_found():
    response = client.get("/pushdown_automaton/non_existent_pushdown_automaton/test?input_string=0101")

    assert response.status_code == 404
    assert response.json()['detail'] == {"error": "Automaton not found"}


def test_index_pushdown_automaton():
    client.post("/pushdown_automaton/", json=pushdown_automaton_data)

    response = client.get("/pushdown_automaton")

    assert response.status_code == 200
    assert response.json()["pushdown_automaton_1"]["name"] == "pushdown_automaton_1"

def test_visualize_pushdown_automaton():
    client.post("/pushdown_automaton", json=pushdown_automaton_data)

    file_path = f"./gui/assets/pushdown_automaton_1_pda_visualization.png"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(b"fake image data")

    response = client.get("/pushdown_automaton/pushdown_automaton_1/visualize")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "image/png+xml"

    os.remove(file_path)

def test_visualize_pushdown_automaton_not_found():

    file_path = f"./gui/assets/pushdown_automaton_1_pda_visualization.png"
    if os.path.exists(file_path):
        os.remove(file_path)
    response = client.get("/pushdown_automaton/pushdown_automaton_1/visualize")
    assert response.status_code == 404
    assert response.json()['detail'] == {"error": "Visualization not found"}


def test_show_pushdown_automaton():
    client.post("/pushdown_automaton", json=pushdown_automaton_data)

    response = client.get("/pushdown_automaton/pushdown_automaton_1")

    assert response.status_code == 200
    print(response.json())
    assert response.json()["name"] == "pushdown_automaton_1"
