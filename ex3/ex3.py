
# Задание 3

def encrypt(text: str, key: str):
    encrypted_text = ''
    for i in range(len(text)):
        a = ord(text[i])
        b = ord(key[i % len(key)]) # циклично берем символы из гаммы
        encrypted_text += chr(a ^ b)
    return(encrypted_text)


message = '''Введите режим работы программы:
1 - Шифрование текста из open_text.txt
2 - Расшифрование текста из encrypted_text.txt
q - выход
>>> '''


while True:
    s = input(message)
    match s:
        case '1':
            with open("ex3/open_text.txt", "r") as open_file, open("ex3/encrypted_text.txt", "w") as encrypted_file:
                key = input('Введите ключ (гамму): ')
                open_text = open_file.read()
                encrypted_text = encrypt(open_text, key)
                encrypted_file.write(encrypted_text)
                print('Результат шифрования помещен в encrypted_text.txt')

        case '2':
            with open("ex3/encrypted_text.txt", "r") as encrypted_file, open("ex3/decrypted_text.txt", "w") as decrypted_file:
                key = input('Введите ключ (гамму): ')
                encrypted_text = encrypted_file.read()
                decrypted_text = encrypt(encrypted_text, key)
                decrypted_file.write(decrypted_text)
                print('Результат расшифрования помещен в decrypted_text.txt')

        case 'q':
            print('До свидания!')
            break
        case _:
            print('Неправильный ввод!')