def encrypt(key, message):
    """
    Шифрует сообщение 'message' с помощью ключа 'key'.
    Ключ является строкой произвольной длины.
    """
    # Преобразуем ключ в список ASCII-кодов символов
    key_codes = [ord(char) for char in key]
    
    # Применяем сдвиг к каждому символу сообщения
    encrypted_message = ''.join(
        chr((ord(char) + key_codes[i % len(key_codes)]) % 65536)
        for i, char in enumerate(message)
    )
    
    return encrypted_message

def decrypt(key, ciphertext):
    """
    Дешифрует зашифрованное сообщение 'ciphertext' с помощью ключа 'key'.
    Ключ является строкой произвольной длины.
    """
    # Преобразуем ключ в список ASCII-кодов символов
    key_codes = [ord(char) for char in key]
    
    # Применяем обратный сдвиг к каждому символу зашифрованного сообщения
    decrypted_message = ''.join(
        chr((ord(char) - key_codes[i % len(key_codes)]) % 65536)
        for i, char in enumerate(ciphertext)
    )
    
    return decrypted_message

# Пример использования
message = input("Введите сообщение: ")
key = input("Введите ключ: ")

encrypted_message = encrypt(key, message)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = decrypt(key, encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)