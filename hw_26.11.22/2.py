"""Сложность O(n)"""


def getMaximumGenerated(n):
    if n <= 1:
        return n
    # Cписок с первыми элементами последовательностb
    nums = [0, 1]
    # Задаем переменную для записи максимума
    tor = 1
    # Запускаем цикл до n, без первых элементов
    for i in range(2, n + 1):
        if i % 2 == 0:       # Если i четное, то добавляем число из списка nums с индексом i//2
            nums.append(nums[i // 2])
        else:                # В другом случае добавляем сумму чисел из списка nums с индексами i // 2 и i//2 + 1
            nums.append(nums[i // 2] + nums[i // 2 + 1])
        tor = max(tor, nums[-1])
    # Возвращаем результат
    return tor


print(getMaximumGenerated(7))