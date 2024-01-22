from typing import List


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    A = [[float('inf')] * n for _ in range(n)]
    for edge in edges:
        u = edge[0]
        v = edge[1]
        wei = edge[2]
        A[u][v] = wei
        A[v][u] = wei
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    A[i][j] = 0
                else:
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
    ind = -1
    mini = float('inf')
    for i in range(n):
        cnt = 0
        for j in range(n):
            if A[i][j] <= distanceThreshold and i != j:
                cnt += 1
        if cnt <= mini:
            ind = i
            mini = cnt
    return ind
