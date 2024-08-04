# задание №1
cycle_counter = 0

while True:
    try:
        input1 = input("введите любое целое число")
        enter_check = int(input1)
        for i in input1:
            if i == "6" or i == "3":
                continue
            print(i, end="")
        print(end="\n")
        break
    except ValueError:
        print("Нужно вводить число!")


# задание №2

sum_numbers = 0
maximum_number = None
minimum_number = None

while True:
    try:
        input2 = int(input("Введите число!"))
        if cycle_counter == 0:
            maximum_number = input2
            minimum_number = input2
        cycle_counter += 1
        sum_numbers += input2
        if input2 == 7:
            print("Good bye!")
            break
        if input2 > maximum_number:
            maximum_number = input2
        if input2 < minimum_number:
            minimum_number = input2
        print(f"Сумма введённых чисел = {sum_numbers}, максимальное введённое число: {maximum_number},"
              f" минимальное введённое число: {minimum_number}, вы ввели {cycle_counter} чисел")
    except ValueError:
        print("Нужно вводить число!")

# задание №3

while True:
    try:
        input_beginning_range = int(input("введите начало диапазона"))
        input_end_range = int(input("введите конец диапазона"))
        if input_beginning_range == input_end_range:
            print("числа должны быть разными!")
        elif input_end_range < input_beginning_range:
            end_range = input_beginning_range
            beginning_range = input_end_range
        else:
            end_range = input_end_range
            beginning_range = input_beginning_range
        end_range += 1
        for a in range(beginning_range, end_range):
            if a % 3 == 0 and a % 5 == 0:
                print("FizzBuzz")
                continue
            if a % 3 == 0:
                print("Fizz")
                continue
            if a % 5 == 0:
                print("Buzz")
                continue
            else:
                print(a)
        break
    except ValueError:
        print("Нужно вводить число")
