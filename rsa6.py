import random
import math

class ExtendedPrecisionInteger:
    def __init__(self, value):
        self.value = value

    def is_odd(self, base=10):
        #Checks if the integer is odd in any base.
        return self.value % base == 1

    def greater(self, other):
        if len(str(self.value)) > len(str(other.value)):
            return True
        elif len(str(self.value)) < len(str(other.value)):
            return False
        for i in range(max(len(str(self.value)), len(str(other.value))) - 1, -1, -1):
            if int(str(self.value)[i]) > int(str(other.value)[i]):
                return True
            elif int(str(self.value)[i]) < int(str(other.value)[i]):
                return False
        return self.value == other.value

    def less(self, other):
        return self.value < other.value

    def equal(self, other):
        return self.value == other.value

    def subtract(self, other):
        if self.value < other.value:
            raise ValueError("Cannot subtract a larger number from a smaller one")
        return ExtendedPrecisionInteger(self.value - other.value)

    def multiply(self, other):
        return ExtendedPrecisionInteger(self.value * other.value)

    def divide(self, other):
        q = 0
        r = self
        while r.greater(other) or r.equal(other):
            q += 1
            r = r.subtract(other)
        return (ExtendedPrecisionInteger(q), r)

    @staticmethod
    def random(n):
        value = random.randint(10**(n-1), 10**n - 1)
        return ExtendedPrecisionInteger(value)

def is_prime(number):
    if number < 2:
        return False    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if(d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse not found")

def rsa_encrypt(message, e, n):
    message_encoded = [ord(c) for c in message]
    ciphertext = [pow(c, e, n) for c in message_encoded]
    return ciphertext

def rsa_decrypt(ciphertext, d, n):
    message_encoded = [pow(c, d, n) for c in ciphertext]
    message = "".join([chr(c) for c in message_encoded])
    return message

# Generating primes
p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)
while p == q:
    q = generate_prime(1000, 5000)

# Calculating n and phi_n
n = p * q
phi_n = (p - 1) * (q - 1)

# Generating e and d
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)
d = mod_inverse(e, phi_n)

print("Public key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("phi_n: ", phi_n)
print("p: ", p)
print("q: ", q)

# Encrypting and Decrypting a message
message = input("Enter your message: ")
encrypted = rsa_encrypt(message, e, n)
print("Encrypted message: ", encrypted)
decrypted = rsa_decrypt(encrypted, d, n)
print("Decrypted message: ", decrypted)