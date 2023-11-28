from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            queue.extend((neighbor, path + [neighbor]) for neighbor in graph[current] if neighbor not in visited)

    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start_node = 'A'
goal_node = 'H'
shortest_path = bfs_shortest_path(graph, start_node, goal_node)

if shortest_path:
    print(f"Shortest path Using BFS from {start_node} to {goal_node}: {shortest_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
