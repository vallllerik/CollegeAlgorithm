# Делаем перебор камней и ищем совпадение драгоценного с обычным
# Сложность


def jewels_in_stones(J, S): # создаем функцию
    jewels_in_collection = 0  #создаем счетчик - для подсчета количества драгоценностей, найденных в коллекции
    for i in J: # перебираем каждый драгоценный камень
        for item in S: # перебираем каждый обычный камень
            if i == item: # если оказывается совпадение
                jewels_in_collection += 1 # счетчик увеличивается
    return jewels_in_collection # возвращаем счетчик

print(jewels_in_stones('aA', 'aAAbbbb'))