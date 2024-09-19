import networkx as nx
import matplotlib.pyplot as plt

def visualize_network_topology(network_topology):
    G = nx.Graph()
    for node in network_topology['nodes']:
        G.add_node(node['id'])
    for edge in network_topology['edges']:
        G.add_edge(edge['from'], edge['to'], weight=edge['cost'])

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

# Load the network topology
network_topology = __import__('network_topology').network_topology

# Visualize the network topology
visualize_network_topology(network_topology)