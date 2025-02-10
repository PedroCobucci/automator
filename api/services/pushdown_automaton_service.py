from models.pushdown_automaton import PushdownAutomaton

def create_pushdown_automaton(data):
    pa = PushdownAutomaton(
        states=set(data["states"]),
        input_symbols=set(data["input_symbols"]),
        stack_symbols=set(data["stack_symbols"]),
        transitions=data["transitions"],
        initial_state=data["initial_state"],
        initial_stack_symbol=data["initial_stack_symbol"],
        final_states=set(data["final_states"]),
        name=data["name"]
    )

    pa.save_diagram()

    return {
        "automaton": pa,
        "states": pa.__dict__["automaton"].states,
        "input_symbols": pa.__dict__["automaton"].input_symbols,
        "stack_symbols": pa.__dict__["automaton"].stack_symbols,
        "transitions": pa.__dict__["automaton"].transitions,
        "initial_state": pa.__dict__["automaton"].initial_state,
        "initial_stack_symbol": pa.__dict__["automaton"].initial_stack_symbol,
        "final_states": pa.__dict__["automaton"].final_states,
        "acceptance_mode": pa.__dict__["automaton"].acceptance_mode,
        "name": pa.__dict__["name"]
    }