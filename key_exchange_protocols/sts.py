from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh


# Key generation
parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
private_key_a = parameters.generate_private_key()
public_key_a = private_key_a.public_key()

private_key_b = parameters.generate_private_key()
public_key_b = private_key_b.public_key()

# Key exchange
shared_key_a = private_key_a.exchange(public_key_b)
shared_key_b = private_key_b.exchange(public_key_a)

print("Shared key A:", shared_key_a)
print("Shared key B:", shared_key_b)
