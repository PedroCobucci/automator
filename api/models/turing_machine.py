from automata.tm.dtm import DTM

class TuringMachine:
    def __init__(self, states, input_symbols, tape_symbols, transitions, initial_state, blank_symbol, final_states, name):
        self.automaton = DTM(
            states=states,
            input_symbols=input_symbols,
            tape_symbols=tape_symbols,
            transitions=transitions,
            initial_state=initial_state,
            blank_symbol=blank_symbol,
            final_states=final_states
        )
        self.name = name

    def accepts(self, input_string):
        return self.automaton.accepts_input(input_string)