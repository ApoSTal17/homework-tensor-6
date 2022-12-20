
# Задание 3

def encrypt(text: str, key: str) -> str:
    encrypted_text = ''
    for i in range(len(text)):
        a = ord(text[i])
        b = ord(key[i % len(key)]) # циклично берем символы из гаммы
        encrypted_text += chr(a ^ b)
    return(encrypted_text)

# С русскими символами в гамме так и не получилось сделать стабильную работу:
# Буквально единицы символов неправильно расшифровываются, так и не удалось выявить закономерность.
# Но с английскими работает как надо. 

message = '''Введите режим работы программы:
1 - Шифрование текста из open_text.txt
2 - Расшифрование текста из encrypted_text.txt
q - выход
>>> '''

while True:
    s = input(message)
    match s:
        case '1':
            with open("ex3/open_text.txt", "r", encoding='utf-8') as open_file, open("ex3/encrypted_text.txt", "w", encoding='utf-8') as encrypted_file:
                key = input('Введите ключ-строку (гамму) (желательно на английском): ')
                open_text = open_file.read()
                encrypted_text = encrypt(open_text, key)
                encrypted_file.write(encrypted_text)
                print('Результат шифрования помещен в encrypted_text.txt')

        case '2':
            with open("ex3/encrypted_text.txt", "r", encoding='utf-8') as encrypted_file, open("ex3/decrypted_text.txt", "w", encoding='utf-8') as decrypted_file:
                key = input('Введите ключ-строку (гамму) (желательно на английском): ')
                encrypted_text = encrypted_file.read()
                decrypted_text = encrypt(encrypted_text, key)
                decrypted_file.write(decrypted_text)
                print('Результат расшифрования помещен в decrypted_text.txt')

        case 'q':
            print('До свидания!')
            break
        case _:
            print('Неправильный ввод!')