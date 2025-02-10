from fastapi import FastAPI
from routes.pushdown_automaton_router import router as pushdown_router
from routes.finite_automaton_router import router as finite_router
from routes.turing_machine_router import router as turing_router
import sys
import os

app = FastAPI()

app.include_router(turing_router, tags=["Turing Machine"])
app.include_router(pushdown_router, tags=["Pushdown Automaton"])
app.include_router(finite_router, tags=["Deterministic Finite Automaton"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Automaton API!"}
