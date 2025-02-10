from models.turing_machine import TuringMachine

def create_turing_machine(data):
    tm = TuringMachine(
        states=set(data["states"]),
        input_symbols=set(data["input_symbols"]),
        tape_symbols=set(data["tape_symbols"]),
        transitions=data["transitions"],
        initial_state=data["initial_state"],
        blank_symbol=data["blank_symbol"],
        final_states=set(data["final_states"]),
        name=data["name"]
    )

    return {
        "states": tm.__dict__["automaton"].states,
        "input_symbols": tm.__dict__["automaton"].input_symbols,
        "tape_symbols": tm.__dict__["automaton"].tape_symbols,
        "transitions": tm.__dict__["automaton"].transitions,
        "initial_state": tm.__dict__["automaton"].initial_state,
        "blank_symbol": tm.__dict__["automaton"].blank_symbol,
        "final_states": tm.__dict__["automaton"].final_states,
        "name": tm.__dict__["name"]
    }