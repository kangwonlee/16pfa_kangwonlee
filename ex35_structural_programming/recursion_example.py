def factorial(n):
    if 1 == n:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
