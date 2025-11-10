# breath first search implementation for graph traversal
from collections import deque
def bfg(graph, start_node):
    """performs bfs starting from a given node,
    Args:
        graph(dict): the graph reprresented as an adjacency list, keys ae nodes, vakues arre list neighbos nodes.
        start_node: the node to stat the traversal from.
    """
    # 1. Initialization...
    # use a set to keep trace of visited node(O(1)) lookups
    visited = set()
    # use a deque for bfs queue
    queue= deque([start_node])
    # mark the sttart_node as visited 
    visited.add(start_node)
    #list to store the prder of visited nodes
    traversal_order = []
    #2. main bfs loop
    while queue:
        # deque the first node
        current_node = queue.popleft()
        traversal_order.append(current_node)
        # get all neighbors of the current node
        print(f"Visiting Node: {current_node}")
        if current_node in graph:
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return traversal_order


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# run BFS and capture the traversal order
traversal_order = bfg(graph, 'A')
print("BFS Traversal Order:", traversal_order)
