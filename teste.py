from graphviz import Digraph

def generate_dtm_diagram(states, transitions, initial_state, final_states):
    dot = Digraph()

    # Adiciona os estados ao grafo
    for state in states:
        if state in final_states:
            dot.node(state, shape="doublecircle", color="green")  # Estado final
        else:
            dot.node(state)

    # Adiciona as transições
    for state, trans in transitions.items():
        for symbol, (next_state, action) in trans.items():
            dot.edge(state, next_state, label=f"Read: {symbol}, Write: {action[0]}, Move: {action[1]}")

    # Define o estado inicial
    dot.node(initial_state, shape="ellipse", color="blue")  # Estado inicial

    return dot

# Exemplo de dados
states = ["q0", "q1"]
transitions = {
    "q0": {"a": ("q1", ("b", "R")), "b": ("q0", ("b", "L"))},
    "q1": {"a": ("q1", ("a", "L")), "b": ("q0", ("b", "R"))}
}
initial_state = "q0"
final_states = ["q1"]

# Gerar e renderizar o diagrama
dtm_diagram = generate_dtm_diagram(states, transitions, initial_state, final_states)
dtm_diagram.render("dtm_diagram", format="png", view=True)
