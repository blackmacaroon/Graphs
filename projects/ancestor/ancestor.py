from util import Queue
'''
# Make a graph
# Traverse the graph with BFS
# Looking for shortest paths between any 2 nodes
# Keep track of the lengths of these paths
# And return where the longest path ends
# If there are no parents, return -1
# If it is a tie, return the lowest node number
'''
ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Cannot create edge based on given vertices") 

def earliest_ancestor(ancestors, starting_node):
    graf = Graph()
    qq = Queue()
        

print(earliest_ancestor(ancestors, 0))