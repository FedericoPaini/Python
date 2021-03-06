"""
Solution to the 'Play on Words' puzzle.
 
The idea is to view the problem as determining the existence
of an Eulerian path in a graph: each word is taken to be
a directed edge, from the node corresponding to the first
character in the word to the node corresponding to the last
character. The words can be arranged into the desired sequence/
pattern only if there exists a path that traverses each edge of
the corresponding graph exactly once (i.e. Eulerian path).
 
"""
 
import sys
 
class nodeInfo:
    def __init__(self):
        self.edges = set()
        self.in_degree = 0
        self.out_degree = 0
        self.visited = False
 
    def addOutEdge(self,vertex):
        self.edges.add(vertex)
        self.out_degree += 1
 
    def addInEdge(self):
        self.in_degree += 1
 
    def markVisited(self):
        self.visited = True
 
    def isVisited(self):
        return self.visited
 
    def unmarkVisited(self):
        self.visited = False
 
    def getInDegree(self):
        return self.in_degree
 
    def getOutDegree(self):
        return self.out_degree
 
    def __str__(self):
        return str(self.edges)+' V:'+str(self.visited)+' In:'+str(self.in_degree)+' Out:'+str(self.out_degree)
 
def isConnected(graph, startAt):
    ''' Perform depth first traversal starting from startAt:
    If num_visited_nodes == num_all_nodes_in_graph,
    then return True.
    '''
    if startAt not in graph.keys():
    # This should never happen.
        return False
    if len(graph.keys()) == 0:
        return False # An empty graph is not connected.
    if len(graph.keys()) == 1:
        return True # A graph with exactly one node is connected.
    to_explore = []
    startAtInfo = graph[startAt]
    startAtInfo.markVisited()
    to_explore.append(startAtInfo)
    visited_count = 1
    while len(to_explore) != 0:
        curInfo = to_explore.pop()
        for node in curInfo.edges:
            nodeInfo = graph.get(node, None)
            if (nodeInfo is None) or nodeInfo.isVisited():
            # 1. There exists an edge to a non-existent node.
            # This should not happen, but it doesn't affect connectedness.
            # OR
            # 2. Node has been visited, so dont revisit.
                continue
            nodeInfo.markVisited()
            to_explore.append(nodeInfo)
            visited_count += 1
 
    if visited_count == len(graph.keys()):
        # connected graph!
        return True
    return False
 
def eulerWalk(graph):
    ''' Return True if an Eulerian path exists in this graph.'''
# Conditions necessary for an Eulerian path in directed graphs:
# 1. graph is connected, AND
# 2. for all nodes except possibly 2, indegree = outdegree, AND
# for those two nodes, one must have indegree = outdegree + 1
# and the other outdegree = indegree + 1
    inequalInOut = []
    for node in graph.keys():
        nodeInfo = graph[node]
        indegree = nodeInfo.getInDegree()
        outdegree = nodeInfo.getOutDegree()
        if not indegree == outdegree:
            inequalInOut.append((node,indegree,outdegree))
 
    if len(inequalInOut) == 0:
        return isConnected(graph,graph.keys()[0])
    if len(inequalInOut) == 2:
        (n1,in1,out1) = inequalInOut[0]
        (n2,in2,out2) = inequalInOut[1]
        if ((in1 == out1+1) and (out2 == in2+1)):
        # n2 = start of path (if graph is connected)
            return isConnected(graph,n2)
        elif ((in2 == out2+1) and (out1 == in1+1)):
    # n1 = start of path (if graph is connected)
            return isConnected(graph,n1)
        return False
 
inputF = sys.stdin # read from stdin
numTestCases = int(inputF.readline())
for i in range(numTestCases): # iterate (by test case) through file
 
    numWordPlates = int(inputF.readline())
    graph = {} # graph: maps node_name --> object of type nodeInfo
 
    for j in range(numWordPlates):
        word = inputF.readline().strip()
        firstChar = word[0]
        lastChar = word[-1]
 
        if firstChar == lastChar:
            charInfo = graph.get(firstChar, None)
            if charInfo is None:
                    charInfo = nodeInfo()
            charInfo.addOutEdge(firstChar)
            charInfo.addInEdge()
            graph[firstChar] = charInfo
        else:
            firstInfo = graph.get(firstChar, None)
            lastInfo = graph.get(lastChar, None)
            if firstInfo is None:
                firstInfo = nodeInfo()
            if lastInfo is None:
                lastInfo = nodeInfo()
            firstInfo.addOutEdge(lastChar)
            lastInfo.addInEdge()
            graph[firstChar] = firstInfo
            graph[lastChar] = lastInfo
 
    if numWordPlates <= 1:
    # Zero or one plate(s).
        print "Ordering is possible."
    elif eulerWalk(graph):
        print "Ordering is possible."
    else:
        print "The door cannot be opened."