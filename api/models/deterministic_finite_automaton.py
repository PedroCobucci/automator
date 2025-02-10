from automata.fa.dfa import DFA
import sys
import os


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
        diagram_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../gui/assets/{self.name}_visualization.png'))
        self.automaton.show_diagram(path=diagram_path)
    