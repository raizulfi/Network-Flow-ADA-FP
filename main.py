from Dinic import Dinic
from FordFulkerson import Graph

# Example 1
n = 6
vertex = [(0, 1, 10), (0, 2, 5), (1, 2, 15), (1, 3, 10), (2, 3, 10), (2, 4, 10), (3, 4, 5), (4, 5, 10)]
source = 0
sink = 5

# Example 2


# Example Usage of Ford-Fulkerson 
print("---------------------------Ford-Fulkerson---------------------------")
example_1 = Graph(n)

for i in vertex:
    example_1.add_edge(i[0], i[1], i[2])

max_flow = example_1.ford_fulkerson(source, sink)

print("\nMaximum Flow:", max_flow)

# Example usage of Dinic
print("---------------------------Dinic's---------------------------")
dinic = Dinic(n, vertex)

max_flow = dinic.max_flow(source, sink)
print(f"Maximum flow: {max_flow}")