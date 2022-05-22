cryptMode = input("Напишите: [Ш]ифрование: ").upper()
if cryptMode not in ['Ш']:
    print("Ошибка, режим не найден!");
    raise SystemExit

startMessage = input("Введите сообщение: ").upper()
keyMessage = input("Введите номер ключа: ")


def encryptDecrypt(mode, message, key, final=""):
    key *= len(message) // len(key) + 1
    for index, symbol in enumerate(message):
        if mode == 'Ш':
            temp = ord(symbol) + int(key[index]) - 13
        final += chr(temp % 30 + ord('А'))
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage, keyMessage))