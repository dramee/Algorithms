arr = [7, 1, 5, 3, 6, 4]


def max_profit(prices):

    s = 0

    for i in range(len(prices) - 1):

        if prices[i + 1] > prices[i]:
            s += prices[i + 1] - prices[i]

    return s


print(max_profit(arr))



