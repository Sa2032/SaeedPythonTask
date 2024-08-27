import math
def is_prime(n):
    if n < 2:
        return []
    sqrt_n = int(math.sqrt(n))
    result = [(n % i == 0, i) for i in range(2, sqrt_n + 1)]
    return result
print(is_prime(7))  
print(is_prime(28))  
