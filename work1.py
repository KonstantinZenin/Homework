while True:
    try:
        degrees_celsius = int(input("Введите градусы цельсия: "))
        break
    except ValueError:
        print("Нужно вводить число")

degrees_fahrenheit = 1.8 * degrees_celsius + 32

print(degrees_fahrenheit)
