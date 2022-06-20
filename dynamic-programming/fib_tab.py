def fib(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


if __name__ == '__main__':
    print(fib(6))
    print(fib(50))
