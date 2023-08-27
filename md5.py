import hashlib

# Text for hashing
data = b"Hello, MD5!"

# Create object of hash-function MD5
hash_object = hashlib.md5()

# Update object with data
hash_object.update(data)

# Get hash in bytes
hash_bytes = hash_object.digest()

# Convert the hash to a string of hexadecimal characters
hash_hex = hash_object.hexdigest()

print("Hash in bytes:", hash_bytes)
print("Hash as a string:", hash_hex)
