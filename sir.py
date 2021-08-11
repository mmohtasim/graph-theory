import networkx as nx
import random


def Code():
    G = nx.Graph()
    v = random.randint(1, 10)
    G.add_nodes_from(list(range(1, v + 1)))
    e = 0
    for i in range(v + 1):
        for j in range(i + 1, v + 1):
            k = random.randint(0, 2)
            if k == 1:
                e += 1
                G.add_edge(i, j)

    E = G.number_of_edges()

    degree = G.degree

    max_degree = max(degree, key=lambda i: i[1])[0]

    left_subgraph = [n for n in list(G.nodes()) if n != max_degree]
    right_subgraph = [n for n in list(G.nodes()) if n == max_degree]

    left_subgraph_copy = left_subgraph.copy()

    for i in left_subgraph_copy:
        locale_degree = len([n for n in G.neighbors(i) if n in left_subgraph])
        foreign_degree = len([n for n in G.neighbors(i) if n in right_subgraph])
        if locale_degree > foreign_degree:
            left_subgraph.remove(i)
            right_subgraph.append(i)

    G.remove_edges_from(
        [e for e in G.edges() if e[0] in left_subgraph and e[1] in left_subgraph]
    )
    G.remove_edges_from(
        [e for e in G.edges() if e[0] in right_subgraph and e[1] in right_subgraph]
    )

    x = G.number_of_edges()

    if x >= E / 2:
        return 1
    else:
        return 0


score = 0
for i in range(1000):
    score += Code()

print(score)