def uniquePathsWithObstacles(obstacleGrid):
    # Создаем матрицу
    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    # Первый элемент спика = 1
    dp[0][0] = 1
    # Проход по всему списку
    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])):
            # Если находится камень камень
            if obstacleGrid[i][j] == 1:
                # Отмечаем в матрице камень
                dp[i][j] = 0
            else:
                # Если индекс > 0
                if i > 0 or j > 0:
                    # То прибавляем путей в матрицу
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    # Выводим последний элемент матрицы
    return dp[-1][-1]


print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))