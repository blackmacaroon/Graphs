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


def island_counter(matrix):
    # create a visited matrix
    visited = []
    for i in range (len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # if not visited
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    #run dft and mark as visited
                    dft(x, y, matrix, visited)
                    island_count += 1
    return island_count

def dft(x, y, matrix, visited):
    stak = Stack()
    # because ((tuples))
    stak.push((x, y))

    while stak.size() > 0:
        vertex = stak.pop()
        x , y = vertex
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x,y), matrix):
                stak.push(neighbor)
    return visited

#set of rules used to find neighbors
def get_neighbors(vertex, graph_matrix):
    x, y = vertex
    neighbors = []
    #north
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    #south
    if y < len(graph_matrix) -1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    #east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    #west
    if x > 0 and graph_matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    return neighbors


islands1 = [[0, 1, 0, 1, 0, "spaghetti"],
           [1, 1, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [1, 1, 0, 1, 0, 1]]
islands2 = [[0, 1, 0, 1],
           [1, 1, 0, 1],
           [0, 0, 1, 0],
           [1, 0, 1, 0],
           [1, 1, 0, 1]]
islands3 = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 0],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 1],
           [1, 1, 0, 1, 0]]
islands4 = [[0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
           [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
           [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
           [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
           [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
           [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]


print(island_counter(islands1))
print(island_counter(islands2))
print(island_counter(islands3))
print(island_counter(islands4))

