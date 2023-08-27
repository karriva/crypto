import hashlib

from Crypto.Hash import SHA256


def pycryptodome_sha256():
    # Text for hashing
    data = b"Hello, SHA-256!"

    # Create hash function object SHA-256
    hash_object = SHA256.new(data)

    # Get hash as bytes
    hash_bytes = hash_object.digest()

    # Convert the hash to a string of hexadecimal characters
    hash_hex = hash_object.hexdigest()

    print("Hash in bytes:", hash_bytes)
    print("Hash as a string:", hash_hex)


def easy_sha256():
    # Text for hashing
    data = b"Hello, SHA-256!"

    # Create hash function object SHA-256
    hash_object = hashlib.sha256()

    # Update hash function object with data
    hash_object.update(data)

    # Get the hash as bytes
    hash_bytes = hash_object.digest()

    # Convert the hash to a string of hexadecimal characters
    hash_hex = hash_object.hexdigest()

    print("Hash in bytes:", hash_bytes)
    print("Hash as a string:", hash_hex)


if __name__ == "__main__":
    easy_sha256()
    pycryptodome_sha256()
