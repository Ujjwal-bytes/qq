from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': [],
'F': ['G'],
'G': []

}
bfs(graph,"A")

def dfs(graph, node, visited):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                dfs(graph, neighbor, visited)
graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': ['F'],
'F': []
}
visited = set()
print("DFS TRAVERSAL")
dfs(graph, 'A', visited)
