def conflict(row1, col1, row2, col2):
    """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
    return (
        row1 == row2  # same row
        # or col1 == col2  # same column
        or row1 - col1 == row2 - col2  # same \ diagonal
        or row1 + col1 == row2 + col2
    )  # same / diagonal


def h(state):
    """Return number of conflicting queens for a given node.
    state: a list of length 'n' for n-queens problem,
    where the c-th element of the list holds the value for the row number of the queen in column c.
    """
    N = len(state)
    num_conflicts = 0
    for c1 in range(N):
        for c2 in range(c1 + 1, N):
            num_conflicts += conflict(state[c1], c1, state[c2], c2)
    return num_conflicts


if __name__ == "__main__":
    # print(h([2, 4, 7, 4, 8, 5, 5, 2]))
    # print(h([3, 2, 7, 5, 2, 4, 1, 1]))
    # print(h([2, 4, 4, 1, 5, 1, 2, 4]))
    # print(h([3, 2, 5, 4, 3, 2, 1, 3]))

    # print(h([3, 1, 3, 1]))

    # Q5_1 = [
    #     [0, 1, 3, 1],
    #     [1, 1, 3, 1],
    #     [2, 1, 3, 1],
    #     [3, 0, 3, 1],
    #     [3, 2, 3, 1],
    #     [3, 3, 3, 1],
    #     [3, 1, 0, 1],
    #     [3, 1, 1, 1],
    #     [3, 1, 2, 1],
    #     [3, 1, 3, 0],
    #     [3, 1, 3, 2],
    #     [3, 1, 3, 3],
    # ]
    # print([h(state) for state in Q5_1])

    Q5_2 = [
        [0, 0, 3, 1],
        [1, 0, 3, 1],
        [2, 0, 3, 1],
        [3, 1, 3, 1],
        [3, 2, 3, 1],
        [3, 3, 3, 1],
        [3, 0, 0, 1],
        [3, 0, 1, 1],
        [3, 0, 2, 1],
        [3, 0, 3, 0],
        [3, 0, 3, 2],
        [3, 0, 3, 3],
    ]
    print([h(state) for state in Q5_2])

    # population = [
    #     [2, 4, 7, 4, 8, 5, 5, 2],
    #     [3, 2, 7, 5, 2, 4, 1, 1],
    #     [2, 4, 4, 1, 5, 1, 2, 4],
    #     [3, 2, 5, 4, 3, 2, 1, 3],
    # ]
    # print([h(state) for state in population])
