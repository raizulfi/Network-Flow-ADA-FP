from collections import deque

class Dinic:
    def __init__(self, n, edges):
        """
        Constructor for the Dinic class.
        Args:
            n: Number of nodes in the network.
            edges: List of tuples representing edges, each tuple with format (source, target, capacity).
        """
        self.n = n
        self.graph = [[0] * n for _ in range(n)]  # Residual capacity matrix.
        for u, v, cap in edges:
            self.graph[u][v] = cap  # Forward capacity.
            self.graph[v][u] = 0  # Initially no backward capacity.
    
    def bfs(self, s, t):
        """
        Perform a Breadth-First Search (BFS) to assign levels to nodes.
        Args:
            s: Source node.
            t: Sink node.
        Returns:
            level: List of levels assigned to each node.
        """
        visited = [False] * self.n
        level = [float('inf')] * self.n
        level[s] = 0
        queue = deque()
        queue.append(s)
        while queue:
            u = queue.popleft()
            visited[u] = True
            for v in range(self.n):
                if not visited[v] and self.graph[u][v] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level
    
    def dfs(self, u, t, level, min_flow):
        """
        Perform a Depth-First Search (DFS) to find an augmenting path from u to t.
        Args:
            u: Current node in the search.
            t: Sink node.
            level: List of levels assigned to nodes.
            min_flow: Minimum potential flow that can be pushed through the path.
        Returns:
            flow: Amount of flow actually pushed through the path.
        """
        if u == t:
            return min_flow  # Maximum flow reached the sink.
        for v in range(self.n):
            if level[u] < level[v] and self.graph[u][v] > 0:
                flow = min(min_flow, self.graph[u][v])  # Limit flow by residual capacity.
                residual_flow = self.dfs(v, t, level, flow)
                if residual_flow > 0:  # Found a valid augmenting path.
                    self.graph[u][v] -= residual_flow  # Update forward capacity.
                    self.graph[v][u] += residual_flow  # Update backward capacity.
                    return residual_flow
        return 0  # No valid augmenting path found from this node.
   
    def max_flow(self, s, t):
        """
        Find the maximum flow from source s to sink t in the network.
        Args:
            s: Source node.
            t: Sink node.
        Returns:
            max_flow: Total amount of flow achieved.
        """
        max_flow = 0
        while True:
            level = self.bfs(s, t)  # Assign levels to nodes.
            if level[t] == float('inf'):  # No path from source to sink exists.
                break
            flow = self.dfs(s, t, level, float('inf'))  # Find and push flow through an augmenting path.
            if flow == 0:  # No further flow augmentation possible.
                break
            max_flow += flow  # Update total flow achieved
        
            self.visualize_graph()
        return max_flow

    def visualize_graph(self):
        print("\nResidual Graph:")
        for i in self.graph:
            for j in i:
                print(f"{j:3}", end= " ")
            print()
