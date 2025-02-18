import networkx as nx
import matplotlib.pyplot as plt
from CayleyGraph import CayleyGraph
import Groups

# D4 Group
d8Elements, d8Mult, d8Gen = Groups.DihedralGroup(4)

D8_CGraph = CayleyGraph(d8Elements, d8Mult, d8Gen)
D8_CGraph.build_graph()
D8_CGraph.draw(layout="circular", save_as="D8_Graph.png")

# Integers mod 5 under addition :)
z5Elements, z5Mult, z5Gen = Groups.CyclicGroup(5)

Z5_CGraph = CayleyGraph(z5Elements, z5Mult, z5Gen)
Z5_CGraph.build_graph()
Z5_CGraph.draw(layout="circular", save_as="Z5_Graph.png")

# Symetric group of 3 elements
s3Elements, s3Mult, s3Gen = Groups.S3Group

S3_CGraph = CayleyGraph(s3Elements, s3Mult, s3Gen)
S3_CGraph.build_graph()
S3_CGraph.draw(layout="circular", save_as="S3_Graph.png")

# Quaternion Group Q8
q8Elements, q8Mult, q8Gen = Groups.Q8Group

Q8_CGraph = CayleyGraph(q8Elements, q8Mult, q8Gen)
Q8_CGraph.build_graph()
Q8_CGraph.draw(layout="circular", save_as="Q8_Graph.png")
