import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.vertices
        max_flow = 0

        while True:
            # Run BFS to find augmenting paths
            visited = [False] * self.vertices
            queue = [source]
            visited[source] = True

            while queue:
                u = queue.pop(0)

                for v, capacity in enumerate(self.graph[u]):
                    if not visited[v] and capacity > 0:
                        queue.append(v)
                        visited[v] = True
                        parent[v] = u

            # If no augmenting path is found, break the loop
            if not visited[sink]:
                break

            # Find the minimum capacity in the augmenting path
            path_flow = sys.maxsize
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Update capacities in the residual graph
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            # Visualize the residual graph
            self.visualize_residual_graph(source, sink)

        return max_flow

    def visualize_residual_graph(self, source, sink):
        print("\nResidual Graph:")
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(f"{self.graph[i][j]:3}", end=" ")
            print()