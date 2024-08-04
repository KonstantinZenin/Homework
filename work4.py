alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
input_text = input("Введите текст: ")
while True:
    try:
        input_key = int(input("Введите шаг сдвига: "))
        break
    except ValueError:
        print("Нужно вводить цифру!")

if input_key < 1:
    input_key = input_key * -1

if input_key > 52:
    input_key = input_key % 52


def incryption_function(text, key):
    incryption_text = ""
    for letter in text:
        position = alphabet.find(letter)
        new_position = position + key
        if letter in alphabet:
            incryption_text += alphabet[new_position]
        else:
            incryption_text += letter
    return incryption_text


def decryption_function(text, key):
    decryption_text = ""
    for letter in text:
        position = alphabet.find(letter)
        new_position = position - key
        if letter in alphabet:
            decryption_text += alphabet[new_position]
        else:
            decryption_text += letter
    return decryption_text


incryption_text_value = incryption_function(input_text, input_key)
decryption_text_value = decryption_function(incryption_text_value, input_key)
print(incryption_text_value)
print(decryption_text_value)
