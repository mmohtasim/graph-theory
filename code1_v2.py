import networkx as nx 
import networkx.drawing
import matplotlib.pyplot as plt 

# if you use G = nx.complete_graph() for testing please remove until line 13

# G= nx.Graph() 

# v, e = map(int, input("Enter v and e(space seperated):").split())
# G.add_nodes_from(list(range(1,v+1)))

# for _ in range(e):
#     G.add_edge(*tuple(map(int,input("input edged(space separated):").split())))

# G= nx.complete_graph(20)
G = nx.Graph()
G.add_edges_from([(1,6),(1,3),(1,4),(1,5),(1,2),(6,3),(6,4)])

v = G.number_of_nodes()
degree = G.degree

max_degree = max(degree, key= lambda i:i[1])[0]

left_subgraph = [ n for n in list(G.nodes()) if n != max_degree ]
right_subgraph= [ n for n in list(G.nodes()) if n == max_degree ]

for i in left_subgraph:
    locale_degree = len([n for n in G.neighbors(i) if n in  left_subgraph])
    foreign_degree= len([n for n in G.neighbors(i) if n in right_subgraph])
    if  locale_degree > foreign_degree :
        left_subgraph.remove(i)
        right_subgraph.append(i)

plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')

G.remove_edges_from([e for e in G.edges() if e[0] in  left_subgraph and e[1] in  left_subgraph])
G.remove_edges_from([e for e in G.edges() if e[0] in right_subgraph and e[1] in right_subgraph])

top = nx.bipartite.sets(G)[0]
pos = nx.bipartite_layout(G, top)

plt.subplot(122)
nx.draw(G,pos, with_labels=True, font_weight='bold')
plt.show()
