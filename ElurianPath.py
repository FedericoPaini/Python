# Copyright 2013 Gabriel Bianconi, http://www.gabrielbianconi.com/
#
# This work is licensed under the Creative Commons 
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 
# Finds an Eulerian path in a given graph. Returns None if no
# such path exists.
 
def find_eulerian_path(graph):
 
    # The number of edges in the graph
    edges = len(graph)
 
    # Create a dictionary with the degree of each node
    degrees = {}
 
    for edge in graph:
        for node in edge:
            if node in degrees:
                degrees[node] += 1
            else:
                degrees[node] = 1
 
    # Determine how many nodes have odd degree
    odd_nodes = 0
    for node in degrees:
        if degrees[node] % 2 == 1:
            odd_nodes += 1
 
    # Return None if the graph doesn't contain an Eulerian path.
    # A graph only has an Eulerian path if the number of nodes
    # with odd degree is 0 or 2
    if odd_nodes != 2 and odd_nodes != 0:
        return None
 
    # A list of the steps of the Eulerian path
    path = []
 
    # If there are odd nodes, the path must start with an odd node
    for node in degrees:
        if degrees[node] % 2 == 1:
            # Start with an arbitrary path, not necessarily Eulerian
            # The first and final nodes have odd degree
            path = find_arbitrary_path(graph, node)
            break
 
    # If there are no odd nodes, start with an arbitrary node
    if len(path) == 0:
        path = find_arbitrary_path(graph, graph[0][0])
 
    # If the current path does not contain all nodes, there are missing inner, closed paths
    while len(path) < (edges + 1):
 
        # Determine a node which has missing edges in the path
        current_node = None
        for node in path:
            if degrees[node] > (path.count(node) + 1):
                current_node = node
                break
 
        # The index of this node in the path
        node_index = path.index(current_node)
        # An arbitrary, closed path containing the node with the remaining edges
        inner_path = find_arbitrary_path(graph, current_node)
        # Add the closed path to the current path
        path = path[:node_index] + inner_path + path[node_index + 1:]
 
    return path
 
# Finds an arbitrary path from a given starting node. If the starting
# node has odd degree, the path will end with a node of odd degree.
# Otherwise,the path will be closed. The used edges are removed from
# the graph variable.
 
def find_arbitrary_path(graph, starting_node):
 
    path = [starting_node]
 
    # If there are unused edges, find edges connected to the last node
    # and add the connected node to the path
    while len(graph):
 
        for i in range(len(graph)):
            if graph[i][0] == path[-1]:
                path.append(graph[i][1])
                graph.pop(i)
                break
            elif graph[i][1] == path[-1]:
                path.append(graph[i][0])
                graph.pop(i)
                break
            # If there are no such edges, the path can't be continued
            # and is returned
            elif i == len(graph) - 1:
                return path
 
    # If all edges have been used, return the path
    return path
 
# Examples:
 
print find_eulerian_path([(1, 2), (2, 3), (3, 1)])
print find_eulerian_path([(1, 2), (1, 3), (1, 5), (2, 3), (3, 4), (3, 5), (4, 5)])
print find_eulerian_path([(1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (4, 5)])
print find_eulerian_path([(1, 13), (1, 6), (6, 11), (3, 13),
    (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
    (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
    (7, 14), (10, 13)])