import networkx as nx

# G = nx.Graph()

# v, e = map(int, input("Enter v and e(space seperated):").split())
# G.add_nodes_from(list(range(1, v + 1)))

# for _ in range(e):
#     G.add_edge(*tuple(map(int, input("input edged(space separated):").split())))

G = nx.complete_graph(6)

v = G.number_of_nodes()
degree = G.degree

max_degree = max(degree, key=lambda i: i[1])[0]

left_subgraph = [n for n in list(G.nodes()) if n != max_degree]
right_subgraph = [n for n in list(G.nodes()) if n == max_degree]

left_subgraph_copy = left_subgraph.copy()

for i in left_subgraph_copy:
    if len([n for n in G.neighbors(i) if n in left_subgraph]) > len(
        [n for n in G.neighbors(i) if n in right_subgraph]
    ):
        left_subgraph.remove(i)
        right_subgraph.append(i)

print(left_subgraph)
print(right_subgraph)

G.remove_edges_from(
    [e for e in G.edges() if e[0] in left_subgraph and e[1] in left_subgraph]
)
G.remove_edges_from(
    [e for e in G.edges() if e[0] in right_subgraph and e[1] in right_subgraph]
)

# print(len(left_subgraph))
# print(*left_subgraph)
# print(len(right_subgraph))
# print(*right_subgraph)
# print(G.number_of_edges())
