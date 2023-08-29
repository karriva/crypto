import random
from sympy import nextprime, primitive_root


# Generate a random number
def generate_random():
    return random.randint(1, 1000)


# Generate keys
def generate_keys(p, g, private):
    public = pow(g, private, p)
    return public


# Encryption
def encrypt(p, g, public, message):
    k = generate_random()
    c1 = pow(g, k, p)
    s = pow(public, k, p)
    c2 = (message * s) % p
    return c1, c2


# Decryption
def decrypt(p, private, c1, c2):
    s = pow(c1, private, p)
    s_inv = pow(s, -1, p)
    message = (c2 * s_inv) % p
    return message


# Example usage
if __name__ == "__main__":
    p = nextprime(1000)  # Prime number p
    g = primitive_root(p)  # Primitive root modulo p
    private = generate_random()  # Private key

    public = generate_keys(p, g, private)
    message = 42  # Message to encrypt

    c1, c2 = encrypt(p, g, public, message)
    decrypted_message = decrypt(p, private, c1, c2)

    print("Original message:", message)
    print("Decrypted message:", decrypted_message)
