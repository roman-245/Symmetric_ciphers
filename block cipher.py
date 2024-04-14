from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_cbc(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return cipher.iv, ciphertext

def decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    return unpad(plaintext, AES.block_size)

# Функция для удаления паддинга
def unpad(data, blocksize):
    if not data:
        return data
    padding = data[-1]
    if isinstance(padding, int):
        padding = padding & 0xFF
    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding")
    return data[:-padding]

# Пример использования
key = get_random_bytes(16)  # Генерируем случайный ключ
plaintext = b'This is a secret message'
iv, ciphertext = encrypt_cbc(plaintext, key)

decrypted_text = decrypt_cbc(ciphertext, key, iv)
print("Расшифрованный текст:", decrypted_text.decode())
