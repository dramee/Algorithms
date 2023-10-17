def numTrees(n: int) -> int:
    # 1 -> 1
    # 2 -> 2
    a = [0] * (n + 1)
    for i in range(n + 1):
        if i <= 1:
            a[i] = 1
        else:
            res = 0
            for j in range((i + 1) // 2):
                k = i - 1 - j
                if j != k:
                    res += 2 * a[j] * a[k]
                else:
                    res += a[j] * a[k]
            a[i] = res
    return a[n]


print(numTrees(4))
