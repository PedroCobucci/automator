from fastapi import APIRouter, HTTPException
from services.turing_machine_service import create_turing_machine

router = APIRouter()

automata_store = {}
automata_data = {}

@router.post("/turing_machine/")
def create_tm(data: dict):
    automaton = create_turing_machine(data)
    automata_store[data["name"]] = automaton.copy()
    automaton.pop("automaton", None)
    automata_data[data["name"]] = automaton
    return {"message": "Turing Machine created successfully!"}

@router.get("/turing_machine/{name}/test")
def test_tm(name: str, input_string: str):
    if name not in automata_store:
        raise HTTPException(status_code=404, detail={"error": "Automaton not found"})
    return {"accepted": automata_store[name]["automaton"].accepts(input_string)}

@router.get("/turing_machine")
def index_turing_machine():
    return automata_data

@router.get("/turing_machine/{name}")
def show_turing_machine(name: str):
    return automata_data[f"{name}"]