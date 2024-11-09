 max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and go up to the root
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]
build_max_heap(arr)
print ("Task_1 :Use python to implement the max-heapify verbatim from the slide.")
print ("-------------------------------------------------------------------------")
print ("                                                                         ")
print("Max heap array:", arr)



# Define the Node and Graph classes
class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Node({self.value})"

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        if value not in self.adjacency_list:
            self.adjacency_list[value] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.adjacency_list and to_node in self.adjacency_list:
            self.adjacency_list[from_node].append(to_node)
            self.adjacency_list[to_node].append(from_node)

    def __str__(self):
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.adjacency_list.items())

# Create a graph and add nodes and edges
g = Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Print the graph to see its adjacency list representation
print ("                                                                         ")
print ("Task 2: Implement a graph using an adjacency list. Use classes to model Graph and Nodes.")
print ("----------------------------------------------------------------------------------------")
print(g)
