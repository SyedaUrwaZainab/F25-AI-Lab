
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path

    if limit == 0:
        for n in graph[node]:
            if n not in path:
                return "CUTOFF", []
        return "FAILURE", []

    cutoff = False

    for n in graph[node]:
        if n not in path:
            result, new_path = dls(n, goal, limit - 1, path + [n])

            if result == "FOUND":
                return result, new_path

            if result == "CUTOFF":
                cutoff = True

    if cutoff:
        return "CUTOFF", []

    return "FAILURE", []


print("DLS RESULTS")

for i in range(1, 5):
    result, path = dls("A", "G", i, ["A"])
    print("Limit:", i, "Result:", result, "Path:", path)


def iddfs(start, goal, max_depth):
    for i in range(max_depth + 1):
        result, path = dls(start, goal, i, [start])
        print("Depth:", i, "Result:", result)

        if result == "FOUND":
            print("Path:", path)
            return

    print("Goal not found")


print("\nIDDFS RESULTS")

for i in range(1, 5):
    print("\nMaximum Depth:", i)
    iddfs("A", "G", i)


print("\nEDGE CASE TESTS")

print("Start equals Goal:", dls("A", "A", 2, ["A"]))

graph["F"] = ["A"]
print("Cycle and Unreachable Goal:", dls("A", "X", 5, ["A"]))
