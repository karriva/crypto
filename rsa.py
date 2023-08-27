from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def pycryptodome_rsa():
    # Generate key pair RSA
    key = RSA.generate(2048)

    # Text for encrypting
    plaintext = b"Hello, RSA!"

    # Create an encryptor object using a public key
    cipher = PKCS1_OAEP.new(key.publickey())

    # Encrypting text
    ciphertext = cipher.encrypt(plaintext)
    print("Encrypted text:", ciphertext)

    # Create a decryptor object using a private key
    decipher = PKCS1_OAEP.new(key)

    # Decrypting key
    decrypted_text = decipher.decrypt(ciphertext)
    print("Decrypted text:", decrypted_text.decode())


def cryptography_rsa():
    # Generating key pair RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Text for encrypting
    plaintext = b"Hello, RSA!"

    # Encrypt text using public key
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Encrypted text:", ciphertext)

    # Decrypt text using private key
    decrypted_text = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Decrypted text:", decrypted_text.decode())


if __name__ == "__main__":
    cryptography_rsa()
    pycryptodome_rsa()
