from cesarfile import *

def encrypt(k, m):
    return ''.join(map(chr, ((x + k)%65536 for x in map(ord, m))))

def decrypt(k, m):
    return ''.join(map(chr, ((x - k)%65536 for x in map(ord, m))))

code = input("Введите текст: ")
key = int(input("Введите смещение: "))
codecs = encrypt(key, code)
decodecs = decrypt(key, codecs)

print(f"Изначальное слово - {code}")
print(f"Зашифрованное слово - {codecs}")
print(f"Дешифрованное слово - {decodecs}")

# Восстановление текста, без знания ключа

cracked_message = crack_caesar_cipher(codecs)
print(f"Дешифрованное слово, без использования ключа (Взломом) - {cracked_message}")
