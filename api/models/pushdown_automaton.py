from automata.pda.dpda import DPDA
import sys
import os


class PushdownAutomaton:
    def __init__(self, states, input_symbols, stack_symbols, transitions, initial_state, initial_stack_symbol, final_states, name):
        self.automaton = DPDA(
            states=states,
            input_symbols=input_symbols,
            stack_symbols=stack_symbols,
            transitions=transitions,
            initial_state=initial_state,
            initial_stack_symbol=initial_stack_symbol,
            final_states=final_states,
            acceptance_mode='final_state'
        )
        self.name = name

    def accepts(self, input_string):
        return self.automaton.accepts_input(input_string)
    
    def save_diagram(self):
        diagram_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../gui/assets/{self.name}_visualization.png'))
        self.automaton.show_diagram(path=diagram_path)