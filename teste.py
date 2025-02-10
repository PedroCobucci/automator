from automata.fa.dfa import DFA
#from automata.visualization import plot_dfa

# Criando um autômato DFA simples
dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q2', 'b': 'q1'},
        'q2': {'a': 'q2', 'b': 'q2'},
    },
    initial_state='q0',
    final_states={'q2'}
)

# Gerando e mostrando o diagrama
dfa.show_diagram(path="teste.png")
