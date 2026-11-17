def alphabeta(depth, node, alpha, beta, is_max, scores, height):
    if depth == height:
        return scores[node]

    if is_max:
        best = -float('inf')

        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            alpha, beta, False, scores, height)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            alpha, beta, True, scores, height)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


scores = [3, 5, 2, 9, 12, 5, 23, 23]
height = 3

result = alphabeta(0, 0, -float('inf'),
                   float('inf'), True, scores, height)

print("The optimal value is:", result)
