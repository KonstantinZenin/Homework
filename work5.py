import string
# Задача №1

user_input_1 = input("Введите строку для проверки на палиндром букв:")
palindrome_answer = False
user_input_1_lower = user_input_1.lower()
palindrome_check = ""
c = 0

for _ in user_input_1_lower:
    ascii_lowercase = string.ascii_lowercase
    if _ in ascii_lowercase:
        palindrome_check += _

stroke_len = len(palindrome_check) - 1
half_stroke_len = int(stroke_len / 2)

while stroke_len > half_stroke_len:

    if palindrome_check[stroke_len] != palindrome_check[c]:
        palindrome_answer = False
    else:
        palindrome_answer = True

    stroke_len -= 1
    c += 1

if palindrome_answer:
    print(f"Буквы в строке :{user_input_1}. Образуют палиндром!")
else:
    print(f"Буквы в строке :{user_input_1}. Не образуют палиндром!")

# задача №2

user_input_2 = input("Введите строку:")
autput_2 = ""
for _ in user_input_2:
    if _ in string.punctuation:
        continue

    autput_2 += _

print(autput_2)

# задача №3
user_input_3 = input("Введите строку:")
nums_list_1 = [i + 1 for i in range(26 * 2)]
autput_3 = ""

for _ in user_input_3:
    if _ in string.ascii_letters:
        a = string.ascii_letters.find(_)
        autput_3 += str(nums_list_1[a])
        autput_3 += "!"
        continue
    autput_3 += _

print(autput_3)
