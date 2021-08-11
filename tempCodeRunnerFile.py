
# for i in left_subgraph:
#     locale_degree = len([n for n in G.neighbors(i) if n in left_subgraph])
#     foreign_degree = len([n for n in G.neighbors(i) if n in right_subgraph])
#     if locale_degree > foreign_degree:
#         left_subgraph.remove(i)
#         right_subgraph.append(i)

# G.remove_edges_from(
#     [e for e in G.edges() if e[0] in left_subgraph and e[1] in left_subgraph]
# )
# G.remove_edges_from(
#     [e for e in G.edges() if e[0] in right_subgraph and e[1] in right_subgraph]
# )

# print(len(left_subgraph))
# print(*left_subgraph)
# print(len(right_subgraph))
# print(*right_subgraph)
# print(G.number_of_edges())