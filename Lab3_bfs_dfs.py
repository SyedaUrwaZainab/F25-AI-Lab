
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def bfs(start, goal):
    q = [[start]]
    seen = []
    order = []

    while q:
        path = q.pop(0)
        node = path[-1]

        if node in seen:
            continue

        seen.append(node)
        order.append(node)

        if node == goal:
            return path, order

        for n in graph[node]:
            q.append(path + [n])

def dfs(start, goal):
    stack = [[start]]
    seen = []
    order = []

    while stack:
        path = stack.pop()
        node = path[-1]

        if node in seen:
            continue

        seen.append(node)
        order.append(node)

        if node == goal:
            return path, order

        for n in reversed(graph[node]):
            stack.append(path + [n])

bfs_path, bfs_order = bfs("A", "G")
dfs_path, dfs_order = dfs("A", "G")

print("BFS Path:", bfs_path)
print("BFS Visit Order:", bfs_order)

print("DFS Path:", dfs_path)
print("DFS Visit Order:", dfs_order)
