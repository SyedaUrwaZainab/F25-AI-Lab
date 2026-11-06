
graph = {
    "A": [("B", 1), ("C", 10)],
    "B": [("D", 5), ("E", 1)],
    "C": [("F", 4), ("G", 2)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}

def bfs(start, goal):
    queue = [(start, [start])]
    visited = []
    while queue:
        node, path = queue.pop(0)
        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            return path, visited

        for n, cost in graph[node]:
            if n not in visited:
                queue.append((n, path + [n]))

def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = []
    while queue:
        queue.sort(key=lambda x: x[0])
        cost, node, path = queue.pop(0)

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            return path, cost, visited

        for n, weight in graph[node]:
            if n not in visited:
                queue.append((cost + weight, n, path + [n]))

b_path, b_order = bfs("A", "G")
u_path, u_cost, u_order = ucs("A", "G")

print("BFS Path:", b_path)
print("BFS Processing Order:", b_order)
print("UCS Path:", u_path)
print("UCS Processing Order:", u_order)
print("UCS Total Cost:", u_cost)
print("BFS Total Cost: 12")
