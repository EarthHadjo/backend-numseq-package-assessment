def fib(n):
    '''Returns the nth Fibonacci number'''
    x = 0
    y = 1
    z = 0
    for _ in range(n):
        x = y
        y = z
        z = x + y
    return z