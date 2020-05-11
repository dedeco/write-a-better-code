def knapsack(capacity, weights, values):
    n = len(values)  # quantity itens
    M = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    weights, values = zip(*sorted(zip(weights, values)))  #sort weights/values (referencing weights)

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                M[i][w] = 0
            elif weights[i - 1] <= w:
                M[i][w] = max(M[i - 1][w], M[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                M[i][w] = M[i - 1][w]
    return M[n][capacity]


if __name__ == '__main__':
    test_case = int(input())
    capacity, qty_items = map(int, input().rstrip().split())
    weights = []
    values = []
    for _ in range(qty_items):
        w, v = map(int, input().rstrip().split())
        weights.append(w)
        values.append(v)

    print(knapsack(capacity, weights, values))
