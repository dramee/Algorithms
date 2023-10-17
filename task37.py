def calc_min_hp(dungeon: list) -> int:
    m, n = len(dungeon), len(dungeon[0])
    dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
    dp[m - 1][n], dp[m][n - 1] = 1, 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

    return int(dp[0][0])


test = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]

print(calc_min_hp(test))
