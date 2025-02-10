from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from services.deterministic_finite_automaton_service import create_dfa

router = APIRouter()

automata_store = {}

def get_automaton(name: str):
    if name not in automata_store:
        raise HTTPException(status_code=404, detail={"error": "Automaton not found"})
    return automata_store[name]

@router.post("/dfa/")
def create_dfa_route(data: dict):
    dfa = create_dfa(data)
    automata_store[data["name"]] = dfa
    return {"message": "Deterministic Finite Automaton created successfully!"}

@router.get("/dfa/{name}/test")
def test_dfa(name: str, input_string: str):
    dfa = get_automaton(name)
    return {"accepted": dfa.accepts(input_string)}

@router.get("/dfa")
def index_dfa():
    return {"automatos": automata_store}

@router.get("/dfa/{name}/visualize")
def visualize_dfa(name: str):
    dfa = get_automaton(name)
    
    file_path = f"./gui/assets/{name}_visualization.png"
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail={"error": "Visualization not found"})
    
    return FileResponse(file_path, media_type="image/png+xml")
