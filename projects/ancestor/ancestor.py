
'''
depth first search
'''
ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node, visited=None):
    if visited is None:
        visited = set()
        visited.add(starting_node)
        print(starting_node)
        for adjacent in ancestors.vertices[starting_node]:
            if adjacent not in visited:
                ancestors.dft_recursive(adjacent, visited)
