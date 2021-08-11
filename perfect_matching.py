
import networkx as nx
from networkx.algorithms.matching import is_perfect_matching, maximal_matching

G= nx.Graph()

v, e = map(int, input("Enter v and e(space seperated):").split())
G.add_nodes_from(list(range(1,v+1)))

for _ in range(e):
    G.add_edge(*tuple(map(int,input("input edged(space separated):").split())))

if is_perfect_matching(G,maximal_matching(G)):
    print("Bob")
else:
    print("Alice")