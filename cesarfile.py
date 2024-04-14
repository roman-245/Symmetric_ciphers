import string
from collections import Counter

def encrypt(key, plaintext):
    """
    Функция для зашифрования текста с помощью шифра Цезаря.
    
    Args:
        key (int): Ключ шифрования, число в диапазоне от 1 до 26.
        plaintext (str): Исходный текст для зашифрования.
        
    Returns:
        str: Зашифрованный текст.
    """
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(key, ciphertext):
    """
    Функция для расшифрования текста, зашифрованного с помощью шифра Цезаря.
    
    Args:
        key (int): Ключ шифрования, число в диапазоне от 1 до 26.
        ciphertext (str): Зашифрованный текст.
        
    Returns:
        str: Расшифрованный текст.
    """
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def frequency_analysis(text):
    """
    Функция для анализа частоты букв в тексте.
    
    Args:
        text (str): Текст для анализа.
        
    Returns:
        list: Список кортежей (буква, частота), отсортированный по убыванию частоты.
    """
    letters = string.ascii_letters
    text = ''.join([c for c in text if c in letters])
    freqs = Counter(text)
    return freqs.most_common()

def calculate_score(decrypted_text, english_letter_freq):
    """
    Функция для оценки качества расшифрованного текста на основе сравнения
    частоты букв в тексте с эталонной частотой букв в английском языке.
    
    Args:
        decrypted_text (str): Расшифрованный текст.
        english_letter_freq (str): Строка, содержащая эталонную частоту букв в английском языке.
        
    Returns:
        float: Оценка качества расшифрованного текста.
    """
    freqs = frequency_analysis(decrypted_text)
    score = 0
    for i, (char, _) in enumerate(freqs):
        if char.upper() in english_letter_freq:
            score += abs(i - english_letter_freq.index(char.upper()))
    return score

def crack_caesar_cipher(ciphertext):
    """
    Функция для взлома шифра Цезаря путем перебора всех возможных ключей.
    
    Args:
        ciphertext (str): Зашифрованный текст.
        
    Returns:
        str: Расшифрованный текст, если его удалось успешно взломать, или сообщение "Unable to crack the cipher."
    """
    decrypted_texts = []
    for key in range(1, 65536):
        decrypted_text = decrypt(key, ciphertext)
        decrypted_texts.append((key, decrypted_text))
    
    english_letter_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    min_score = float('inf')
    best_key = None
    
    for key, decrypted_text in decrypted_texts:
        score = calculate_score(decrypted_text, english_letter_freq)
        if score < min_score:
            min_score = score
            best_key = key
    
    if best_key is not None:
        return decrypt(best_key, ciphertext)
    else:
        return "Unable to crack the cipher."

def main():
    # Получение имен файлов от пользователя
    input_file_name = input("Введите имя файла для исходного текста: ")
    encrypted_file_name = input("Введите имя файла для зашифрованного текста: ")
    decrypted_file_name = input("Введите имя файла для расшифрованного текста: ")
    cracked_file_name = input("Введите имя файла для взломанного текста: ")

    # Чтение исходного текста из файла
    with open(input_file_name, 'r') as file:
        message = file.read().strip()

    # Выполнение шифрования, расшифрования и взлома
    key = 4
    encrypted_message = encrypt(key, message)
    decrypted_message = decrypt(key, encrypted_message)
    cracked_message = crack_caesar_cipher(encrypted_message)

    # Запись результатов в файлы
    with open(encrypted_file_name, 'w') as file:
        file.write(encrypted_message)

    with open(decrypted_file_name, 'w') as file:
        file.write(decrypted_message)

    with open(cracked_file_name, 'w') as file:
        file.write(cracked_message)

    print("Готово!")