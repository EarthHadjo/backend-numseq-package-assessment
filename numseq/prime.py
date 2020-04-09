def primes(n):
    '''Returns a list of all prime numbers less than n'''
    prime = []
    for x in range(2, n + 1):
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                break
        else:
            prime.append(x)
    return prime


def is_prime(m):
    '''Returns a boolean indicating whether `m` is a prime number'''
    if m in primes(m):
        return True
    return False