from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def pycryptodome_digital_sign():
    # Generate key pair RSA
    key = RSA.generate(2048)

    # Text for sign
    data = b"Hello, digital signature!"

    # Create hash
    hash_obj = SHA256.new(data)

    # Create sign
    signature = pkcs1_15.new(key).sign(hash_obj)

    # Check sign
    try:
        pkcs1_15.new(key.publickey()).verify(hash_obj, signature)
        print("The signature is correct: the data is authentic and complete.")
    except (ValueError, TypeError):
        print("The signature is invalid: the data has been changed or the signature is forged.")


def cryptography_digital_sign():
    # Generate key pair RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Text for sign
    data = b"Hello, digital signature!"

    # Create sign
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Check sign
    try:
        public_key.verify(
            signature,
            data,
            # b'ssfe',
            padding.PSS(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("The signature is correct: the data is authentic and complete.")
    except Exception:
        print("The signature is invalid: the data has been changed or the signature is forged.")


if __name__ == "__main__":
    cryptography_digital_sign()
    pycryptodome_digital_sign()
