from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from services.deterministic_finite_automaton_service import create_finite_automaton

router = APIRouter()

automata_store = {}
automata_data = {}

def get_automaton(name: str):
    if name not in automata_store:
        raise HTTPException(status_code=404, detail={"error": "Automaton not found"})
    return automata_store[name]["automaton"]

@router.post("/finite_automaton/")
def create_finite_automaton_route(data: dict):
    finite_automaton = create_finite_automaton(data)
    automata_store[data["name"]] = finite_automaton.copy()
    finite_automaton.pop("automaton", None)
    automata_data[data["name"]] = finite_automaton
    return {"message": "Deterministic Finite Automaton created successfully!"}

@router.get("/finite_automaton/{name}/test")
def test_finite_automaton(name: str, input_string: str):
    finite_automaton = get_automaton(name)
    return {"accepted": finite_automaton.accepts(input_string)}

@router.get("/finite_automaton")
def index_finite_automaton():
    return automata_data

@router.get("/finite_automaton/{name}/visualize")
def visualize_finite_automaton(name: str):
    finite_automaton = get_automaton(name)
    
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../gui/assets/{name}_dfa_visualization.png'))
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail={"error": "Visualization not found"})
    
    return FileResponse(file_path, media_type="image/png+xml")

@router.get("/finite_automaton/{name}")
def show_dfa(name: str):
    if name not in automata_data:
        raise HTTPException(status_code=404, detail={"error": "Automaton not found"})
    return automata_data[f"{name}"]
