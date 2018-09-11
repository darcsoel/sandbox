class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.visited = [False] * len(self.matrix)
        self.stable = [False] * len(self.matrix)

    def calculate(self):
        for vehicle, connections in enumerate(self.matrix):
            self.visited[vehicle] = True


graph_matrix = [
    [0, 10, 30, 50, 10],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 10],
    [0, 40, 20, 0, 0],
    [10, 0, 10, 30, 0],
]

dijkstra = Graph(graph_matrix)
print(dijkstra.calculate())
