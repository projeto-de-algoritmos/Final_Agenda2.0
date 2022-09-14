from event import Event
from datetime import datetime, timedelta
from dateutil import parser
import networkx as nx
import matplotlib.pyplot as plt
import sys

# nos e arestas do grafo
nodes = ['grafos1', 'grafos2', 'greed', 'dc', 'pd']
edges = [(('grafos1', 'grafos2'), 1), (('grafos1','greed'), 2), (('grafos1', 'dc'), 4), (('grafos2', 'greed'), 2), (('grafos2', 'dc'), 4), (('greed', 'dc'), 3), (('dc', 'pd'), 4)]

#directed graph with weight
class Graph():
    def __init__(self):
        self.G = nx.DiGraph()
        self.add_nodes()
        self.add_edges()

    def add_nodes(self):
        for node in nodes:
            self.G.add_node(node)


    def add_edges(self):
        for edge in edges:
            self.G.add_edge(edge[0][0], edge[0][1], weight=edge[1])

    def get_graph(self):
        return self.G

    def get_nodes(self):
        return self.G.nodes()

    def get_edges(self):
        return self.G.edges()

    def get_weight(self, node1, node2):
        return self.G[node1][node2]['weight']

    def print_graph(self):
        print(self.G.edges.data('weight'))

    def draw_graph(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_size=1500, node_color='skyblue', edge_color='black', width=1, alpha=0.7)
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_color='red')
        plt.show()

    def get_shortest_path(self, node1, node2):
        return nx.dijkstra_path(self.G, node1, node2)



#Test event list
events = [Event(deadline=parser.parse('2020-10-10'), duration=0, description=['Grafos_1','Grafos_2','Dividir_e_Conquistar'], name='Trabalho 1'),
Event(deadline=parser.parse('2020-10-10'), duration=0, description=['Grafos_1','Dividir_e_Conquistar'], name='Trabalho 2')]

graph = Graph()

graph.print_graph()
graph.draw_graph()



