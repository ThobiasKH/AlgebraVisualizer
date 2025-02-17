import networkx as nx
import matplotlib.pyplot as plt
from CayleyGraph import CayleyGraph
import Groups

# D4 Group
d4Elements, d4Mult, d4Gen = Groups.DihedralGroup(4)

D4_CGraph = CayleyGraph(d4Elements, d4Mult, d4Gen)
D4_CGraph.build_graph()
D4_CGraph.draw(layout="circular", save_as="D4_Graph.png")

z5Elements, z5Mult, z5Gen = Groups.CyclicGroup(5)

Z5_CGraph = CayleyGraph(z5Elements, z5Mult, z5Gen)
Z5_CGraph.build_graph()
Z5_CGraph.draw(layout="circular", save_as="Z5_Graph.png")
