# Lab 4 Task 2: A* and UCS on the same campus graph

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}      
zero_h = {"S": 0, "A": 0, "B": 0, "C": 0, "G": 0}  

def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]   
    best = {start: 0}                      
    trace = []                             
    expanded = 0                           
    stale = 0                             

    while pq:
        pq.sort()                          
        f, g, node, path = pq.pop(0)

        if g != best[node]:               
            stale = stale + 1
            continue

        trace.append(node)

        if node == goal:                 
            return g, path, trace, expanded, stale

        expanded = expanded + 1

        for nxt, w in graph[node]:
            ng = g + w
            if nxt not in best or ng < best[nxt]:
                best[nxt] = ng
                pq.append((ng + h[nxt], ng, nxt, path + [nxt]))

    return None, [], trace, expanded, stale


def path_cost(graph, path):
    total = 0
    for i in range(len(path) - 1):
        for nxt, w in graph[path[i]]:
            if nxt == path[i + 1]:
                total = total + w
    return total


print("A* SEARCH")
g, path, trace, expanded, stale = astar(graph, h, "S", "G")
print("Path:", path)
print("Returned cost:", g)
print("Path cost check:", path_cost(graph, path))
print("Processed nodes:", trace)
print("Expansion count:", expanded)
print("Stale entries skipped:", stale)

print("\nUCS SEARCH (h = 0)")
g, path, trace, expanded, stale = astar(graph, zero_h, "S", "G")
print("Path:", path)
print("Returned cost:", g)
print("Path cost check:", path_cost(graph, path))
print("Processed nodes:", trace)
print("Expansion count:", expanded)
print("Stale entries skipped:", stale)