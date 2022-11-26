# сложность   O(n)

def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)): # Запускаем цикл по ценам
        if prices[i] > prices[i - 1]: # Если цена элемента, больше предыдущей итерации
            max_profit += prices[i] - prices[i - 1] # к прибыли прибавляем их разницу
    return max_profit # возвращаем максимальную прибыль


print(maxProfit([7, 1, 5, 3, 6, 4]))