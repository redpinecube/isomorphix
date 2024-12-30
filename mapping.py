import pandas as pd
import networkx as nx

def create_nth_graph(node, n, df):
    """
    for the specified node, create a graph up to its nth neighbour expansion.
    """
    total_nodes = {node}
    current_level = {node}
    i = 0

    while i < n: 
        neighbours = set(df[df["From Node ID"].isin(current_level)]["To Node Id"])
        total_nodes = neighbours | total_nodes
        current_level = neighbours
        i += 1

        if not current_level:
            break
    return df[df["From Node ID"].isin(total_nodes)]

    
def create_sequence(node):
    """
    for the specifed node create a sequence of graphs. 
    """
    pass

def convert_sequence(graph_sequence):
    """
    converts the graph sequence into a matrix sequence.
    """

def compare_nodes(node1, node2):
    """
    compares the matrix sequence of node1 and node1 to generate 
    a similarity sequence. 
    sequence is used to return an overall similarity statistic.
    """
    pass

def compare_all(node, node_list):
    """
    computes the node similarity between node and all nodes in 
    node_list. the node with the lowest similarity is returned. 
    """

def generate_mapping(graph1, graph2):
    """
    return a mapping from graph1 and graph2. 
    """
    pass

