from queue import PriorityQueue

# A* Algorithm
def a_star(graph, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, weight in graph[current]:
            temp_g_score = g_score[current] + weight

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                open_set.put((temp_g_score, neighbor))

    return None


# BFS
def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend([n for n, _ in graph[node]])


# DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

print("A* Path:", a_star(graph, 'A', 'F'))
print("BFS Traversal:", end=" ")
bfs(graph, 'A')
print("\nDFS Traversal:", end=" ")
dfs(graph, 'A')
