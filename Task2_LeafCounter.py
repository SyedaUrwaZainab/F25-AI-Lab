
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
                depth + 1, index * 2 + i, False, scores,
                target, alpha, beta, count
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
                depth + 1, index * 2 + i, True, scores,
                target, alpha, beta, count
            )
            value = min(value, result)
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


# Same scores for both algorithms
scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = int(math.log2(len(scores)))

# Run Minimax
minimax_count = [0]
minimax_value = minimax(0, 0, True, scores, depth, minimax_count)

# Run Alpha-Beta
alphabeta_count = [0]
alphabeta_value = alphabeta(
    0, 0, True, scores, depth,
    float('-inf'), float('inf'), alphabeta_count
)

# Display results
print("Minimax root value:", minimax_value)
print("Minimax leaf evaluations:", minimax_count[0])

print("Alpha-Beta root value:", alphabeta_value)
print("Alpha-Beta leaf evaluations:", alphabeta_count[0])
