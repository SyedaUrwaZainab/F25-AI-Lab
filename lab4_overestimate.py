# Lab 4  Task 3: Overestimate one heuristic value

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}


def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]   
    best = {start: 0}
    trace = []
    expanded = 0

    while pq:
        pq.sort()
        f, g, node, path = pq.pop(0)

        if g != best[node]:                
            continue

        trace.append(node)

        if node == goal:                  
            return g, path, trace, expanded

        expanded = expanded + 1

        for nxt, w in graph[node]:
            ng = g + w
            if nxt not in best or ng < best[nxt]:
                best[nxt] = ng
                pq.append((ng + h[nxt], ng, nxt, path + [nxt]))


# Original run
print("ORIGINAL (h(C) = 2)")
g, path, trace, expanded = astar(graph, h, "S", "G")
print("Path:", path, " Cost:", g)
print("Processed nodes:", trace, " Expansion count:", expanded)

# Change only h(C) from 2 to 10 (true cost of C is 3)
h2 = dict(h)
h2["C"] = 10

print("\nMODIFIED (h(C) = 10)")
g, path, trace, expanded = astar(graph, h2, "S", "G")
print("Path:", path, " Cost:", g)
print("Processed nodes:", trace, " Expansion count:", expanded)