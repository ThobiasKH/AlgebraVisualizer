import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

img_folder = Path(__file__).parent / 'img'

class CayleyGraph:
    def __init__(self, elements, multiplication_table, generators):
        self.elements = elements
        self.multiplication_table = multiplication_table
        self.generators = generators
        self.graph = nx.DiGraph()

    def build_graph(self):
        """Add nodes and edges based on group operation"""
        for elem in self.elements:
            self.graph.add_node(elem)
            for gen in self.generators:
                result = self.multiplication_table[elem][gen]  # Compute multiplication
                self.graph.add_edge(elem, result, label=gen)

    def draw(self, layout="spring", save_as=None):
        """Draw the graph with a specified layout"""
        layouts = {
            "spring": nx.spring_layout,
            "circular": nx.circular_layout,
            "shell": nx.shell_layout
        }
        pos = layouts.get(layout, nx.spring_layout)(self.graph)  # Default to spring layout

        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)

        # Edge labels (showing the generator used)
        edge_labels = {(u, v): d["label"] for u, v, d in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_color='red')

        plt.title("Cayley Graph")
        if save_as:
            plt.savefig(str(img_folder) + "/" + save_as)
        # plt.show() / doesn't work for some reason
