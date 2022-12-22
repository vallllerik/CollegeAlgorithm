def tribonacci(self, n):
    prev1, prev2, prev3 = 0, 1, 1
    if n == 0:
        return prev1
    if n == 1:
        return prev2
    if n == 2:
        return prev3

    output = 0
    for _ in range(3, n + 1):
        output = prev1 + prev2 + prev3
        prev1 = prev2
        prev2 = prev3
        prev3 = output
    return output