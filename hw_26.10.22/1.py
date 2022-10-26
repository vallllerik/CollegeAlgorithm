# Для этой задачи нужно просто следовать указаниям в условии:
# 1. Пока параметр не равен нулю, проверяем, является ли число четным.
# 2. Если число четное - делим на 2. Если нечетное, то вычитаем единицу.
# 3. После каждой операции счетчик увеличивается.
# 4. Когда число дойдет до нуля - возвращаем счетчик.
# Сложность


def numberOfSteps(num): #
    count = 0  # Счетчик количества шагов
    while num != 0:  # пока число не равно нулю
        if num % 2 == 0:  # проверяем является ли число четным
            num //= 2
            count += 1
        else: # в другом случае число является нечетным
            num -= 1
            count += 1
    return count  # возвращаем счетчик

print(numberOfSteps())