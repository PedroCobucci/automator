from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from services.pushdown_automaton_service import create_pushdown_automaton
import os

router = APIRouter()

automata_store = {}

def get_automaton(name: str):
    if name not in automata_store:
        raise HTTPException(status_code=404, detail={"error": "Automaton not found"})
    return automata_store[name]

@router.post("/pushdown_automaton/")
def create_pda(data: dict):
    automaton = create_pushdown_automaton(data)
    automata_store[data["name"]] = automaton
    return {"message": "Pushdown Automaton created successfully!"}

@router.get("/pushdown_automaton/{name}/test")
def test_pda(name: str, input_string: str):
    pda = get_automaton(name)
    return {"accepted": pda.accepts(input_string)}

@router.get("/pushdown_automaton")
def index_pda():
    print(automata_store)
    return automata_store

@router.get("/pushdown_automaton/{name}/visualize")
def visualize_pda(name: str):
    pda = get_automaton(name)
    
    file_path = f"./gui/assets/{name}_visualization.svg"
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail={"error": "Visualization not found"})
    
    return FileResponse(file_path, media_type="image/svg+xml")
