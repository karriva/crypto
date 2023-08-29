from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import hashes

# Generate DH parameters
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Generate private keys for Alice and Bob
private_key_alice = parameters.generate_private_key()
private_key_bob = parameters.generate_private_key()

# Public parameters to be exchanged between Alice and Bob
public_key_alice = private_key_alice.public_key()
public_key_bob = private_key_bob.public_key()

# Public key exchange (in a real scenario, this would be over a network)

# Calculate shared secrets
shared_key_alice = private_key_alice.exchange(public_key_bob)
shared_key_bob = private_key_bob.exchange(public_key_alice)

# Convert shared secrets to actual shared keys
derived_key_alice = hashes.Hash(hashes.SHA256())
derived_key_alice.update(shared_key_alice)
final_key_alice = derived_key_alice.finalize()

derived_key_bob = hashes.Hash(hashes.SHA256())
derived_key_bob.update(shared_key_bob)
final_key_bob = derived_key_bob.finalize()

print("Alice's shared key:", final_key_alice)
print("Bob's shared key:", final_key_bob)
