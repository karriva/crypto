from cryptography.fernet import Fernet

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def pycryptodome_aes():
    # Generate key and random initialization vector (IV)
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    # Create object AES using key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encryption text (pre-added)
    plaintext = b"Hello, AES!"

    # Encrypting text
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    print("Encrypted text:", ciphertext)

    # Decrypting text
    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(decipher.decrypt(ciphertext), AES.block_size)
    print("Decrypted text:", decrypted_text.decode())


def cryptography_aes():
    # Generate key
    key = Fernet.generate_key()

    # Create object Fernet using key
    cipher_suite = Fernet(key)

    # Text for encryption
    plaintext = b"Hello, AES!"

    # Encrypt text
    cipher_text = cipher_suite.encrypt(plaintext)
    print("Encrypted text:", cipher_text)

    # Decrypt text
    decrypted_text = cipher_suite.decrypt(cipher_text)
    print("Decrypted text:", decrypted_text.decode())


if __name__ == "__main__":
    cryptography_aes()
    pycryptodome_aes()
