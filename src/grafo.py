from event import Event
from datetime import datetime, timedelta
from dateutil import parser
import networkx as nx
import matplotlib.pyplot as plt
import sys
from userInterface import TelaAgenda

# nos e arestas do grafo
nodes = ['Grafos_1', 'Grafos_2', 'Greed', 'Dividir_e_Conquistar', 'Progamação_Dinâmica']
edges = [(('Grafos_1', 'Grafos_2'), 1), (('Grafos_1','Greed'), 2), (('Grafos_1', 'Dividir_e_Conquistar'), 4), (('Grafos_2', 'Greed'), 2), (('Grafos_2', 'Dividir_e_Conquistar'), 4), (('Greed', 'Dividir_e_Conquistar'), 3), (('Dividir_e_Conquistar', 'Progamação_Dinâmica'), 4)]

#directed graph with weight
class Graph():
    def __init__(self, events):
        self.G = nx.DiGraph()
        self.add_nodes()
        self.add_edges()
        self.events = events

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

    def set_duration(self):
        for event in self.events:
            #clean event.description of '[' and ']' and '"'
            event.description = event.description.replace('[', '')
            event.description = event.description.replace(']', '')
            event.description = event.description.replace("'", '')
            event.description = event.description.replace(' ', '')
            categories = event.description.split(',')
            print(categories)
            time = 0
            # if there is category Grafos_2 in description there needs to be a Grafos_1 category
            # if there is category Progamação_Dinâmica in description there needs to be a Dividir_e_Conquistar category

            if 'Grafos_2' in categories:
                if 'Grafos_1' not in categories:
                    #insert before Grafos_2
                    categories.insert(categories.index('Grafos_2'), 'Grafos_1')
            if 'Progamação_Dinâmica' in categories:
                if 'Dividir_e_Conquistar' not in categories:
                    #insert before Progamação_Dinâmica
                    categories.insert(categories.index('Progamação_Dinâmica'), 'Dividir_e_Conquistar')


            start = categories[0]
            end = categories[-1]

            # if there is only one category
            if start == end:
                time = self.get_weight(start, end)
            else:
                # find the shortest path between the first and last category
                # the path must contain all categories
                path = nx.shortest_path(self.G, start, end, weight='weight')
                for i in range(len(path)-1):
                    time += self.get_weight(path[i], path[i+1])

            event.set_duration(time)
            # return time

        



# #Test event list
# eventsTest = [Event(deadline=parser.parse('2020-10-10'), duration=0, description='Grafos_1,Grafos_,ividir_e_Conquistar', name='Trabalho 1'),
# Event(deadline=parser.parse('2020-10-10'), duration=0, description='Grafos_1,Dividir_e_Conquistar',nme='Trabalho 2'),
# Event(deadline=parser.parse('2020-10-10'), duration=0, description='Grafos_1,Progamação_Dinâmica', name='Trabalho 3')]
# events = TelaAgenda.start()
# print('Normal',events)
# print('Teste',eventsTest)
# graph = Graph(events)

# # graph.print_graph()
# # graph.draw_graph()
# graph.set_duration()

# for event in events:
    # print(event.duration)