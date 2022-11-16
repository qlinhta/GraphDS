import networkx as nx
import pandas as pd
import numpy as np


def read_graph(path):
    '''
    Read graph from file
    :param path: path to file
    :return: networkx graph
    '''
    edges = pd.read_csv(path)
    graph = nx.from_edgelist(edges.values.tolist())
    return graph


