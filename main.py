class Graph:
    def __init__(self):
        """Initialize an empty graph represented by an adjacency list."""
        self.graph = {}

    def add_edge(self, city1, city2):
        """
        Adds an undirected edge between city1 and city2.

        Parameters:
        - city1 (str): The name of the first city.
        - city2 (str): The name of the second city.
        """
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []
        self.graph[city1].append(city2)
        self.graph[city2].append(city1)

    def build_graph_from_file(self, filename):
        """
        Parses a file and builds the graph based on city connections.

        Parameters:
        - filename (str): The path to the file containing city connections.
        """
        with open(filename, 'r') as file:
            for line in file:
                city1, city2 = line.strip().split(',')
                self.add_edge(city1.strip(), city2.strip())

    def bfs(self, start, goal):
        """
        Perform Breadth-First Search (BFS) to find a path from start to goal.

        Parameters:
        - start (str): Starting city.
        - goal (str): Destination city.

        Returns:
        - list: Path from start to goal if found, else None.
        """
        visited = set()
        queue = [(start, [start])]

        while queue:
            (vertex, path) = queue.pop(0)
            if vertex in visited:
                continue

            for neighbor in self.graph[vertex]:
                if neighbor == goal:
                    return path + [goal]
                else:
                    queue.append((neighbor, path + [neighbor]))
            visited.add(vertex)
        return None

    def dfs(self, start, goal, path=None, visited=None):
        """
        Perform Depth-First Search (DFS) recursively to find a path from start to goal.

        Parameters:
        - start (str): Starting city.
        - goal (str): Destination city.
        - path (list): Current path being explored.
        - visited (set): Set of visited cities.

        Returns:
        - list: Path from start to goal if found, else None.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = [start]
        if start == goal:
            return path

        visited.add(start)
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result = self.dfs(neighbor, goal, path + [neighbor], visited)
                if result is not None:
                    return result
        return None


def max_heapify(arr, n, i):
    """
    Maintain the max-heap property for a subtree rooted at index `i`.

    Parameters:
    - arr (list): List of elements.
    - n (int): Size of the heap.
    - i (int): Root index of the subtree.

    Returns:
    None
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def heapify(arr):
    """
    Convert a list into a max-heap.

    Parameters:
    - arr (list): List of elements.

    Returns:
    None
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heapsort(arr):
    """
    Sorts a list in ascending order using the heapsort algorithm.

    Parameters:
    - arr (list): List of elements to sort.

    Returns:
    None
    """
    n = len(arr)
    heapify(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


if __name__ == "__main__":
    # Sample usage for heap functions
    data = [4, 10, 3, 5, 1]
    print("Original list:", data)
    heapsort(data)
    print("Sorted list:", data)

    # Sample usage for graph and searches
    graph = Graph()
    graph.build_graph_from_file('cities.txt')
    print("BFS path from New York to Houston:", graph.bfs("New York", "Houston"))
    print("DFS path from Seattle to Miami:", graph.dfs("Seattle", "Miami"))
