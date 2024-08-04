# Викторина
counter = 0
cycle_counter = 0

while True:
    try:
        user_answer1 = int(input("Введите любой високосный год"))
        if user_answer1 % 4 == 0 and user_answer1 % 100 != 0:
            counter += 1
            print("Верно!")
        elif (
            user_answer1 % 4 == 0
            and user_answer1 % 100 == 0
            and user_answer1 % 400 == 0
        ):
            counter += 1
            print("Верно!")
        else:
            print("Не угадали!")
        break
    except ValueError:
        print("Нужно вводить число!")

while True:
    try:
        if (
                cycle_counter != 0
        ):
            print("Нужно ввести слово!")
        user_answer2 = input("Какое животное считается лучшим другом человека?")
        int(user_answer2)
        cycle_counter += 1
    except ValueError:
        if (
            user_answer2 == "Собака"
            or user_answer2 == "собака"
            or user_answer2 == "Dog"
            or user_answer2 == "dog"
            or user_answer2 == "Собачка"
            or user_answer2 == "собачка"
        ):
            counter += 1
            print("Верно!")
        else:
            print("Не угадали!")
        cycle_counter = 0
        break

while True:
    try:
        if (
                cycle_counter != 0
        ):
            print("Нуно ввести слово!")
        user_answer3 = input("Что тяжелее 1 килограмм пуха или 1 кг железа?")
        int(user_answer3)
        cycle_counter += 1
    except ValueError:
        if (
            user_answer3 == "Ничего"
            or user_answer3 == "они равны по весу"
            or user_answer3 == "ничего"
            or user_answer3 == "Вес одинаковый"
            or user_answer3 == "одинаково"
            or user_answer3 == "вес одинаковый"
            or user_answer3 == "Одинаково"
        ):
            counter += 1
            print("Верно!")
        else:
            print("Не угадали!")
        cycle_counter = 0
        break

while True:
    try:
        if (
                cycle_counter != 0
        ):
            print("Нуно ввести слово!")
        user_answer4 = input("Какой город является столицей Росии?")
        int(user_answer4)
        cycle_counter += 1
    except ValueError:
        if (
            user_answer4 == "Москва"
        ):
            counter += 1
            print("Верно!")

        elif (
                user_answer4 == "москва"
        ):
            print("Неправильно! Москва пишется с большой буквы!")

        else:
            print("Не угадали!")
        cycle_counter = 0
        break

while True:
    try:
        user_answer5 = input("Сколько будет 2+2*2?")

        if (
            int(user_answer5) == 2 + 2 * 2
        ):
            counter += 1
            print("Верно!")
        else:
            print("Не угадали!")
        break
    except ValueError:
        print("Нужно вводить число!")

while True:
    try:
        if (
                cycle_counter != 0
        ):
            print("Нуно ввести слово!")
        user_answer6 = input("Введите ответ на загадку: Висит груша нельзя скушать!")
        int(user_answer6)
        cycle_counter += 1
    except ValueError:
        if (
            user_answer6 == "Лампочка" or user_answer6 == "лампочка"
        ):
            counter += 1
            print("Верно!")
        else:
            print("Не угадали!")
        cycle_counter = 0
        break

print("Поздравляю вы набрали " + str(counter) + " баллов!")
