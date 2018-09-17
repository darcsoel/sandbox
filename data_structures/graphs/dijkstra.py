import sys


class Graph:
    def __init__(self, matrix, start_from=0):
        self.matrix = matrix
        self.start_from = start_from
        self.visited = [False] * len(self.matrix)
        self.way, self.backup_way = list(), list()
        self.wrong_vehicle = None

    def calculate(self):
        vehicles = {i: True for i in range(len(self.matrix))}
        self.visited[self.start_from] = True
        self.way.insert(0, self.start_from)
        self.backup_way.insert(0, self.start_from)
        del vehicles[self.start_from]

        while len(vehicles) > 0:
            connections = self.matrix[self.start_from]

            if all(connection == 0 for connection in connections) and len(self.way) > 0:
                self.visited[self.start_from] = True
                self.wrong_vehicle = self.start_from
                self.start_from = self.way.pop()
                continue

            min_weight = sys.maxsize
            neighbourhoods = [[closest, weight] for closest, weight in enumerate(connections)
                              if closest != self.start_from and not self.visited[closest]
                              and closest != self.wrong_vehicle]

            closest = None

            for closest_vehicle, weight in neighbourhoods:
                if 0 < weight < min_weight:
                    min_weight = weight
                    closest = closest_vehicle

            if not closest:
                self.wrong_vehicle = self.start_from
                self.start_from = self.backup_way.pop()

            if min_weight != sys.maxsize and closest:
                self.visited[self.start_from] = True
                self.way.insert(0, closest)
                self.backup_way.insert(0, closest)
                self.start_from = closest
                self.wrong_vehicle = None
                del vehicles[self.start_from]

    def print_way(self):
        return self.way


graph_matrix = [
    [0, 10, 30, 50, 10],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 10],
    [0, 40, 20, 0, 0],
    [10, 0, 10, 30, 0],
]

dijkstra = Graph(graph_matrix)
dijkstra.calculate()

print(dijkstra.print_way())
