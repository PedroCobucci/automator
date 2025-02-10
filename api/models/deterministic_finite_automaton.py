from automata.fa.dfa import DFA

class DeterministicFiniteAutomaton:
    def __init__(self, states, input_symbols, transitions, initial_state, final_states, name):
        self.automaton = DFA(
            states=states,
            input_symbols=input_symbols,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )
        self.name = name

    def accepts(self, input_string):
        return self.automaton.accepts_input(input_string)
        
    def save_diagram(self):
        self.automaton.show_diagram(path=f"./gui/assets/{self.name}_visualization.png")
    