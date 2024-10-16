import re
import csv
from typing import Callable


def password_checker(func: Callable[[str], str]) -> Callable[[str], str]:
    """"
    Декоратор для проверки пароля.
    """
    def wrapper(password: str) -> str:
        """"
        Функция для проверки сложности пароля
        """
        if len(password) < 8:
            return 'Пароль должен быть не менее 8 символов'
        elif not re.search(r'\d', password):
            return 'Пароль должен содержать цифры'
        elif not re.search(r'[A-ZА-Я]', password):
            return 'Пароль должен содержать заглавные буквы'
        elif not re.search(r'[a-zа-я]', password):
            return 'Пароль должен содержать строчные буквы'
        elif not re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
            return 'Пароль должен содержать спецсимвол'
        return func(password)

    return wrapper


@password_checker
def register_user(password: str) -> str:
    return 'Пароль принят'


def password_validator(func: Callable[[str, str], str], min_length=8, min_uppercase=1, min_lowercase=1,
                       min_special_chars=1):
    def wrapper(username, password):
        if len(password) < min_length:
            raise ValueError(f'Пароль должен быть не менее {min_length} символов')
        elif len(re.findall(r'[A-ZА-Я]', password)) < min_uppercase:
            raise ValueError(f'Пароль должен быть не менее {min_uppercase} заглавных букв')
        elif sum(1 for s in password if s.islower()) < min_lowercase:
            raise ValueError(f'Пароль должен быть не менее {min_lowercase} строчных букв')
        elif sum(1 for char in password if not char.isalnum()) < min_special_chars:
            raise ValueError(f'Пароль должен содержать не менее {min_special_chars} специальных символов')
        return func(username, password)

    return wrapper


def username_validator(func: Callable[[str, str], str]):
    def wrapper(username, password):
        if ' ' in username:
            raise ValueError('Имя пользователя не должно содержать пробелов')
        return func(username, password)

    return wrapper


@password_validator
@username_validator
def register_user2(username: str, password: str):
    with open("./Data/users_from_work_14.csv", "a", newline="", encoding="UTF-8",) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password])


print(register_user('sa53ers'))

print(register_user('DAMJHGSER'))

print(register_user('bnftggbj12'))

print(register_user('DAMJHGSER214'))

print(register_user('DAMJHGSER214fv'))

print(register_user('Afdjbakjfbvkdjbn2*'))

print("____________________________________________________________________________________________________")

# Тестирование успешного случая
try:
    register_user2("JohnDoe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по паролю...
try:
    register_user2("JohnDoe", "Password123")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по юзернейму...
try:
    register_user2("John Doe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")
