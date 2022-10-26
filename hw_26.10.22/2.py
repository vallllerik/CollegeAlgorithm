# 1. Проверим сколько команд сейчас и какое кол-во - четное или нечетное
# 2. Если четное, то команд и матчей станет меньше в два раза.
# 2.1 Если команд нечетное кол-во, то 1 команда идет сразу в следущий этап, тогда останется (t/2) + 1, а матчей будет сыграно (t - 1)/2
# 3. Возвращаем кол-во матчей
# Сложность равна


def numberOfMatches(t):
    matches = 0                         # вводим счетчик
    while t > 1:                        # пока команд больше 1 (если команда всего одна, то нужно 0 матчей, тк победитель будет единственный)
        if t % 2 != 0:                  # проверим кол-во команд на нечетность
            matches += int(t // 2)      # сыграет половина команд с другой половиной (кроме той, которая сразу идет в след.этап), делим нацело на 2 (округление в меньшую сторону)
            t = int(t // 2) + 1         # кол-во команд равно 'остаток от деления нацело всех изначальных на 2' + 1 команда
        else:                           # если количество команд четное
            matches += int(t / 2)       # то кол-во матчей равно половине от всех команд (играют пополам)
            t = int(t / 2)              # теперь t = половина от изначального кол-ва команд
    return matches                      # возвращаем кол-во матчей


print(numberOfMatches())

