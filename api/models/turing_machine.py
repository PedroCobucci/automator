from automata.tm.dtm import DTM
import sys
from graphviz import Digraph
import os

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

    def save_diagram(self):
        diagram_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../gui/assets/{self.name}_tm_visualization'))
        
        dtm_diagram = Digraph(name=self.name)
        
        for state in self.automaton.states:
            if state in self.automaton.final_states:
                dtm_diagram.node(state, shape='doublecircle')
            else:
                dtm_diagram.node(state, shape='circle')
        
        for state, transitions in self.automaton.transitions.items():
            for input_symbol, (next_state, write_symbol, move_direction) in transitions.items():
                label = f'{input_symbol}/{write_symbol},{move_direction}'
                dtm_diagram.edge(state, next_state, label=label)
        
        dtm_diagram.render(diagram_path, format="png", cleanup=True)