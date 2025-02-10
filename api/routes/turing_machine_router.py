from fastapi import APIRouter, HTTPException
from services.turing_machine_service import create_turing_machine
from fastapi.responses import FileResponse
import sys
import os

router = APIRouter()

automata_store = {}
automata_data = {}

def get_automaton(name: str):
    if name not in automata_store:
        raise HTTPException(status_code=404, detail={"error": "Automaton not found"})
    return automata_store[name]["automaton"]

@router.post("/turing_machine/")
def create_tm(data: dict):
    automaton = create_turing_machine(data)
    automata_store[data["name"]] = automaton.copy()
    automaton.pop("automaton", None)
    automata_data[data["name"]] = automaton
    return {"message": "Turing Machine created successfully!"}

@router.get("/turing_machine/{name}/test")
def test_tm(name: str, input_string: str):
    automaton = get_automaton(name)
    return {"accepted": automaton.accepts(input_string)}

@router.get("/turing_machine")
def index_turing_machine():
    return automata_data

@router.get("/turing_machine/{name}")
def show_turing_machine(name: str):
    return automata_data[f"{name}"]

@router.get("/turing_machine/{name}/visualize")
def visualize_tm(name: str):
    tm = get_automaton(name)
    
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../gui/assets/{name}_tm_visualization.png'))
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail={"error": "Visualization not found"})
    
    return FileResponse(file_path, media_type="image/png+xml")