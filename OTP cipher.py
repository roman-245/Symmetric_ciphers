def otp_encrypt(plaintext, key):
    return bytes([p ^ k for p, k in zip(plaintext, key)])

def otp_decrypt(ciphertext, key):
    return bytes([c ^ k for c, k in zip(ciphertext, key)])

# Пример использования
plaintext = b"Hello, world!"
key = b"supersecretkey"

ciphertext = otp_encrypt(plaintext, key)
print("Зашифрованный текст:", ciphertext)

decrypted_text = otp_decrypt(ciphertext, key)
print("Расшифрованный текст:", decrypted_text)