from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', './')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', './api')))
from api.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def create_dfa_data():
    return {
        "name": "dfa1",
        "states": ["q0", "q1"],
        "input_symbols": ["a", "b"],
        "transitions": {
            "q0": {
                "a": "q1",
                "b": "q0"
            },
            "q1": {
                "a": "q1",
                "b": "q0"
            }
        },
        "initial_state": "q0",
        "final_states": ["q1"]
    }

def test_create_dfa(create_dfa_data):
    response = client.post("/dfa/", json=create_dfa_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Deterministic Finite Automaton created successfully!"}

def test_test_dfa_accepted(create_dfa_data):
    client.post("/dfa/", json=create_dfa_data)

    response = client.get("/dfa/dfa1/test", params={"input_string": "a"})
    assert response.status_code == 200
    assert response.json() == {"accepted": True}

def test_test_dfa_rejected(create_dfa_data):
    client.post("/dfa/", json=create_dfa_data)

    response = client.get("/dfa/dfa1/test", params={"input_string": "ab"})
    assert response.status_code == 200
    assert response.json() == {"accepted": False}

def test_dfa_not_found():
    response = client.get("/dfa/unknown/test", params={"input_string": "a"})
    assert response.status_code == 404
    assert response.json()['detail'] == {"error": "Automaton not found"}

def test_index_dfa(create_dfa_data):
    client.post("/dfa/", json=create_dfa_data)
    response = client.get("/dfa")
    assert response.status_code == 200
    assert "dfa1" in [dfa['name'] for dfa in response.json()['automatos']]

def test_visualize_dfa(create_dfa_data):
    client.post("/dfa/", json=create_dfa_data)

    file_path = f"assets/dfa1_visualization.png"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(b"fake image data")

    response = client.get("/dfa/dfa1/visualize")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "image/png+xml"

    os.remove(file_path)

def test_visualize_dfa_not_found():
    response = client.get("/dfa/dfa1/visualize")
    assert response.status_code == 404
    assert response.json()['detail'] == {"error": "Visualization not found"}