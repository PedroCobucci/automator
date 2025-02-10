from models.deterministic_finite_automaton import DeterministicFiniteAutomaton

def create_finite_automaton(data):
    dfa = DeterministicFiniteAutomaton(
        states=set(data["states"]),
        input_symbols=set(data["input_symbols"]),
        transitions=data["transitions"],
        initial_state=data["initial_state"],
        final_states=set(data["final_states"]),
        name=data["name"]
    )

    dfa.save_diagram()
    
    return {
        "automaton": dfa,
        "states": dfa.__dict__["automaton"].states,
        "input_symbols": dfa.__dict__["automaton"].input_symbols,
        "transitions": dfa.__dict__["automaton"].transitions,
        "initial_state": dfa.__dict__["automaton"].initial_state,
        "final_states": dfa.__dict__["automaton"].final_states,
        "name": dfa.__dict__["name"]
    }
