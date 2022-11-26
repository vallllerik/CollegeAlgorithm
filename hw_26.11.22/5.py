# сложность O(n)

def getDescentPeriods(prices):
    n = len(prices)  # Запишем в n длину prices
    dp = [1] * n

    for i in range(1, n):
        if prices[i] == prices[i - 1] - 1: # Если настоящий элемент совпадает с предидущим - 1
            dp[i] += dp[i - 1] # в элемент добавляем предыдущий

    return sum(dp) # Возвращаем сумму элементов


print(getDescentPeriods([3, 2, 1, 4]))