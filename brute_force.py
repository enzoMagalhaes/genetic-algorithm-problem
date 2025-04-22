items = [
    [40, 2],  # A
    [50, 3],  # B
    [65, 4],  # C
    [80, 5],  # D
    [110, 7],  # E
    [15, 1],  # F
    [90, 6],  # G
    [70, 4.5],  # H
    [60, 3.5],  # I
    [55, 2.5],  # J
]


def dfs(i, w):
    if i == len(items):
        return 0

    return max(
        items[i][0] + dfs(i + 1, w - items[i][1]) if items[i][1] <= w else 0,
        dfs(i + 1, w),
    )


print(dfs(i=0, w=15))
