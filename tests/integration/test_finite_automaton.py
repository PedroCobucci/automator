from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', './api')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', './')))
from api.main import app
import pytest

client = TestClient(app)

create_finite_automaton_data = {
        "name": "finite_automaton_1",
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

def test_create_finite_automaton():
    response = client.post("/finite_automaton/", json=create_finite_automaton_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Deterministic Finite Automaton created successfully!"}

def test_test_finite_automaton_accepted():
    client.post("/finite_automaton/", json=create_finite_automaton_data)

    response = client.get("/finite_automaton/finite_automaton_1/test?input_string=%s" % "a")
    assert response.status_code == 200
    assert response.json() == {"accepted": True}

def test_test_finite_automaton_rejected():
    client.post("/finite_automaton/", json=create_finite_automaton_data)

    response = client.get("/finite_automaton/finite_automaton_1/test", params={"input_string": "ab"})
    assert response.status_code == 200
    assert response.json() == {"accepted": False}

def test_finite_automaton_not_found():
    response = client.get("/finite_automaton/unknown/test", params={"input_string": "a"})
    assert response.status_code == 404
    assert response.json()['detail'] == {"error": "Automaton not found"}

def test_index_finite_automaton():
    client.post("/finite_automaton/", json=create_finite_automaton_data)
    response = client.get("/finite_automaton")
    assert response.status_code == 200
    assert response.json()["finite_automaton_1"]["name"] == "finite_automaton_1"

def test_visualize_finite_automaton():
    client.post("/finite_automaton/", json=create_finite_automaton_data)

    file_path = f"./gui/assets/finite_automaton_1_visualization.png"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(b"fake image data")

    response = client.get("/finite_automaton/finite_automaton_1/visualize")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "image/png+xml"

    os.remove(file_path)

def test_visualize_finite_automaton_not_found():
    file_path = f"./gui/assets/finite_automaton_1_visualization.png"
    if os.path.exists(file_path):
        os.remove(file_path)
    response = client.get("/finite_automaton/finite_automaton_1/visualize")
    assert response.status_code == 404
    assert response.json()['detail'] == {"error": "Visualization not found"}

def test_show_finite_automaton():
    client.post("/finite_automaton/", json=create_finite_automaton_data)

    response = client.get("/finite_automaton/finite_automaton_1")

    assert response.status_code == 200
    print(response.json())
    assert response.json()["name"] == "finite_automaton_1"