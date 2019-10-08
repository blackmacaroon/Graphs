"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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

    def bft(self, starting_vertex):
        # create a queue
        qq = Queue()
        # created a set of visited  nodes
        visited = set()
        # add starting node to queue
        qq.enqueue(starting_vertex)
        # while queue is not empty
        while qq.size() > 0:
            # pop first node out
            vertex = qq.dequeue()
            # if not visited
            if vertex not in visited:
                # mark as visited
                visited.add(vertex)
                print(vertex) # what is it asking us to do, where is the appropriate place to do it
                # get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)
        # go to top of loop

    def dft(self, starting_vertex):
        # create a queue
        stak = Stack()
        # created a set of visited  nodes
        visited = set()
        # add starting node to queue
        stak.push(starting_vertex)
        # while queus is not empty
        while stak.size() > 0:
            # pop first node out (before anything else! so it's not buried!)
            vertex = stak.pop()
            # if not visited
            if vertex not in visited:
                # mark as visited
                visited.add(vertex)
                print(vertex) # what is it asking us to do, where is the appropriate place to do it
                # get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    stak.push(next_vert)
        # go to top of loop

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            # create set of visited nodes (set, each input in unique so we don't repeat visits)
            visited = set()
        # start at first vertex, add to visited and print
        visited.add(starting_vertex)
        print(starting_vertex)
        # repeat for every neighbor, adding to visited set
        for adjacent in self.vertices[starting_vertex]:
            # if we don't have it:
            if adjacent not in visited:
                # call function until we have them all.
                self.dft_recursive(adjacent, visited)
       
    def bfs(self, starting_vertex, destination_vertex):
        # create queue
        qq = Queue()
        # create an empty set for visited nodes
        visited = set()
        # # create an empty list for shortest path
        # path = []
        # add first node to queue
        qq.enqueue([starting_vertex])
        # while queue is not empty
        while qq.size() > 0:
            # remove first node
            path = qq.dequeue()
            # always grab the last node
            vertex = path[-1]
            # if it's the first one, congrats, you found it.
            if vertex == destination_vertex:
                    # print("huh?", path) # what is it asking us to do, where is the appropriate place to do it
                    return path
            # check if it's been visited
            # if not, mark it as visited
            elif vertex not in visited:
                visited.add(vertex)
                # get adjacent edges and add to list
                for adjacent in self.vertices[vertex]:
                    # add to list path until you find the destination
                    mst = list(path)
                    mst.append(adjacent)
                    qq.enqueue(mst)
        # if queue is empty
        return mst

        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
    def dfs(self, starting_vertex, destination_vertex):
        # stak = Stack()
        # visited = set()
        # create an empty list for shortest path
        # stak.push(starting_vertex)
        # while stak.size() > 0:
        #     vertex = stak.pop()
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("start depth first")
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("start breadth first")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("start recursive dft")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("breadth first search", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
