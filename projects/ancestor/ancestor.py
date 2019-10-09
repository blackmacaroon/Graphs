from util import Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Cannot create edge based on given vertices") 



def earliest_ancestor(ancestors, starting_node):
    # build the graph
    graf = Graph()
    for pair in ancestors:
        # adding the vertecies 
        graf.add_vertex(pair[0])
        graf.add_vertex(pair[1])
        # build edges in reverse, swimming upstream. it matters who the parents are, not who the child is
        graf.add_edge(pair[1], pair[0])
    # breadth first search
    # storing the path in a queue
    qq = Queue()
    qq.enqueue([starting_node])
    # what we keep track of to tell us when we're done
    max_path_length = 1
    earliest_ancestor = -1
    while qq.size() > 0:
        path = qq.dequeue()
        vertex = path[-1]
        # in case of a tie
        # If the path is longer or equal and the value is smaller, or if the path is longer, update the ancestor and longer path
        if(len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = vertex
            max_path_length = len(path)
        for relative in graf.vertices[vertex]:
            new_path = list(path)
            new_path.append(relative)
            qq.enqueue(new_path)
    return earliest_ancestor
