# test_graph.py
import pytest
from main import Graph  # Import your Graph class

def test_bfs():
    graph = Graph()
    graph.build_graph_from_file('cities.txt')  # Build the graph using your cities file
    path = graph.bfs("New York", "Houston")  # Check if there's a valid path
    assert path is not None  # Ensure a path exists

def test_dfs():
    graph = Graph()
    graph.build_graph_from_file('cities.txt')
    path = graph.dfs("Seattle", "Miami")  # Check if DFS finds a valid path
    assert path is not None

