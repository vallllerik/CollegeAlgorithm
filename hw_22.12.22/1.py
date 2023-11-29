from typing import List

def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        counter = []
        for city1, city2 in costs:
            counter.append([city2 - city1,city1,city2])
        counter.sort()
        otv = 0
        for i in range(len(counter)):
            if i < len(counter) // 2:
                otv += counter[i][2]
            else:
                otv += counter[i][1]
        return otv