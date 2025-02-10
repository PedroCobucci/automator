import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', './api')))
from main import app

client = TestClient(app)

def test_create_turing_machine():
    data = {
        "name": "turing_machine_01",
        "states": ['q0', 'q1', 'q2', 'q3', 'q4'],
        "input_symbols": ['0', '1'],
        "tape_symbols": ['0', '1', 'x', 'y', '.'],
        "transitions": {
            'q0': {
                '0': ('q1', 'x', 'R'),
                'y': ('q3', 'y', 'R')
            },
            'q1': {
                '0': ('q1', '0', 'R'),
                '1': ('q2', 'y', 'L'),
                'y': ('q1', 'y', 'R')
            },
            'q2': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q3': {
                'y': ('q3', 'y', 'R'),
                '.': ('q4', '.', 'R')
            }
        },
        "initial_state": "q0",
        "blank_symbol": ".",
        "final_states": ['q4']
    }

    response = client.post("/turing_machine/", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Turing Machine created successfully!"}

def test_test_turing_machine():
    data = {
        "name": "turing_machine_01",
        "states": ['q0', 'q1', 'q2', 'q3', 'q4'],
        "input_symbols": ['0', '1'],
        "tape_symbols": ['0', '1', 'x', 'y', '.'],
        "transitions": {
            'q0': {
                '0': ('q1', 'x', 'R'),
                'y': ('q3', 'y', 'R')
            },
            'q1': {
                '0': ('q1', '0', 'R'),
                '1': ('q2', 'y', 'L'),
                'y': ('q1', 'y', 'R')
            },
            'q2': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q3': {
                'y': ('q3', 'y', 'R'),
                '.': ('q4', '.', 'R')
            }
        },
        "initial_state": "q0",
        "blank_symbol": ".",
        "final_states": ['q4']
    }
    client.post("/turing_machine", json=data)

    input_string = "01"
    response = client.get(f"/turing_machine/turing_machine_01/test?input_string=%s" % input_string)

    assert response.status_code == 200
    assert "accepted" in response.json()
    assert response.json()["accepted"] is True

def test_non_existing_turing_machine():
    response = client.get(f"/turing_machine/doidonaaaa/test?input_string=1")

    assert response.status_code == 404
    assert response.json()['detail'] == {"error": "Automaton not found"}
