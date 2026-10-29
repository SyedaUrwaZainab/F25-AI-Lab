
import math

# Minimax with leaf counter
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, count):
    if curDepth == targetDepth:
        count[0] += 1
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False,
                    scores, targetDepth, count),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False,
                    scores, targetDepth, count)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True,
                    scores, targetDepth, count),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True,
                    scores, targetDepth, count)
        )


# Alpha-Beta with leaf counter
def alphabeta(depth, index, maxTurn, scores, target,
              alpha, beta, count):
    if depth == target:
        count[0] += 1
        return scores[index]

    if maxTurn:
        value = float('-inf')

        for i in range(2):
            result = alphabeta(
                depth + 1, index * 2 + i, False,
                scores, target, alpha, beta, count
            )
            value = max(value, result)
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for i in range(2):
            result = alphabeta(
                depth + 1, index * 2 + i, True,
                scores, target, alpha, beta, count
            )
            value = min(value, result)
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


# Original and reordered leaf scores
original_scores = [3, 5, 2, 9, 3, 5, 2, 9]
reordered_scores = [2, 9, 3, 5, 2, 9, 3, 5]

depth = int(math.log2(len(original_scores)))


# Test original branch order
mini_count1 = [0]
mini_value1 = minimax(
    0, 0, True, original_scores, depth, mini_count1
)

ab_count1 = [0]
ab_value1 = alphabeta(
    0, 0, True, original_scores, depth,
    float('-inf'), float('inf'), ab_count1
)


# Test reordered branches
mini_count2 = [0]
mini_value2 = minimax(
    0, 0, True, reordered_scores, depth, mini_count2
)

ab_count2 = [0]
ab_value2 = alphabeta(
    0, 0, True, reordered_scores, depth,
    float('-inf'), float('inf'), ab_count2
)


# Display comparison
print("Original Branch Order")
print("Minimax value:", mini_value1)
print("Minimax leaves:", mini_count1[0])
print("Alpha-Beta value:", ab_value1)
print("Alpha-Beta leaves:", ab_count1[0])

print("\nReordered Branches")
print("Minimax value:", mini_value2)
print("Minimax leaves:", mini_count2[0])
print("Alpha-Beta value:", ab_value2)
print("Alpha-Beta leaves:", ab_count2[0])
