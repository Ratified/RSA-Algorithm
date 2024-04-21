import random
import math

def is_prime(n, k=5):
    #Miller-Rabin primality test
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(digits):
   #Generate a prime number with specified number of digits
    while True:
        n = random.randint(10**(digits-1), 10**digits)
        if is_prime(n):
            return n

def gcd(a, b):
    #Calculate the greatest common divisor of two numbers
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    #Calculate modular inverse using extended Euclidean algorithm
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keys(digits):
    #Generate public and private keys
    p = generate_prime(digits)
    q = generate_prime(digits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

public_key, private_key = generate_keys(100)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)
