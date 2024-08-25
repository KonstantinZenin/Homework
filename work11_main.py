import json
from pprint import pprint
from random import randint

try:
    from Data.cities import cities_list
except ModuleNotFoundError:
    print("Модуль cities не найден, пожалуйста импортируйте его в папку \"Data\" "
          "или укажите корректный путь до него в строке №6")
    exit()


rules = (
    "Правила игры «Города»: Каждый участник называет реально существующий в данный момент времени город"
    " любой существующей страны, название которого начинается на ту букву,"
    "которой оканчивается название предыдущего города. Исключения составляют названия,"
    "оканчивающиеся на твёрдый и мягкий знаки, а также буквы «Ы» и «Й»:"
    "в таких случаях участник называет город на предпоследнюю букву."
    "Ранее названные города нельзя употреблять снова. Первый участник выбирает любой город."
    "Во время игры запрещается пользоваться справочным материалом."
    "Формально игра оканчивается, когда очередной участник не может назвать нового города,"
    "однако из-за продолжительности и монотонности игрового процесса игра может закончиться ничьей"
    )

json_file_path = "./Data/cities.json"

player_input = ""

player_score = 0

computer_score = 0


def writing_cities(cities_list: list):
    """
    Записывает данные из cities_list в файл json
    :param cities_list: список, импортируемый из файла cities.py
    """
    with open(json_file_path, "w", encoding="utf-8") as file:
        json.dump(cities_list, file, ensure_ascii=False, indent=4)


def read_cities() -> set:
    """
    Импортирует данные из файла json
    :return: сет городов
    """
    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            cities_list_from_json = json.load(file)
            cities_set = {city["name"].lower() for city in cities_list_from_json}
            return cities_set
    except FileNotFoundError:
        writing_cities(cities_list)
        with open(json_file_path, "r", encoding="utf-8") as file:
            cities_list_from_json = json.load(file)
            cities_set = {city["name"].lower() for city in cities_list_from_json}
            return cities_set


cities_set: set = read_cities()

player_cities: set = set()

computer_cities: set = set()

bad_letters: set = set()

turn = 200

for city in cities_set:
    last_letter = city[-1]
    for city_2 in cities_set:
        first_letter = city_2[0]
        if last_letter == first_letter:
            break
    else:
        bad_letters.add(last_letter)

last_letter_1 = ""


def determining_last_letter(city: str):
    """
    Функция определяет последнюю букву в названом городе
    :param city: Названый город
    """
    global last_letter_1
    indent = -1
    if city[-1] in bad_letters:
        indent -= 1
        last_letter_1 = city[indent]
    else:
        last_letter_1 = city[indent]


def determining_first_turn() -> int:
    """
    Функция генерирует случайное число для определения первого хода
    :return: случайное число от 0 до 10
    """
    first_turn = randint(0, 10)
    return first_turn


def find_cities_help() -> set:
    """
    Функция формирует подсказку для хода игрока
    :return: сет с городами, которые можно назвать.
    """
    global last_letter_1
    alphabet = {
        "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
        "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"
    }
    if last_letter_1 == "":
        while last_letter_1 == "" or last_letter_1 in bad_letters:
            last_letter_1 = alphabet.pop()
    cities_help_set = {city for city in cities_set if last_letter_1 == city[0]}
    return cities_help_set


def player_turn() -> tuple:
    """
    Ход игрока
    :return: кортеж с данными хода игрока
    """
    name = "игрок"
    help_1 = find_cities_help()
    pprint(help_1)
    player_input = input("Введите название города")
    city = player_input.lower()
    turn = 0
    return city, name, turn


def computer_turn() -> tuple:
    """
    Ход компьютера
    :return: кортеж с данными хода компьютера
    """
    global city
    name = "компьютер"
    computer_turn_set = find_cities_help()
    if len(computer_turn_set) == 0:
        city = "проиграл"
    else:
        city = computer_turn_set.pop()
    turn = 8
    return city, name, turn


def game():
    """
    Базовая версия игры
    """
    global turn
    if turn == 200:
        turn = determining_first_turn()

    while cities_set:
        if turn < 5:
            value = computer_turn()
            city = value[0]
            turn = value[2]
            # name = value[1]
            try:
                cities_set.remove(city)
            except KeyError:
                pprint(f"Поздравляю! вы победили в игре в города назвав следующие города: {player_cities}"
                       f"а компьютер: {computer_cities}")
                exit()
            determining_last_letter(city)
            computer_cities.add(city)
            print(f"Компьютер назвал город {city}, значит вам нужно назвать город,"
                  f"начинающийся на букву {last_letter_1}")
        else:
            value = player_turn()
            city = value[0]
            turn = value[2]
            # name = value[1]
            if city == "стоп":
                pprint(f"Вы решили сдаться и проиграли!"
                       f"Вы смогли назвать следующие города: {player_cities}, а компьютер: {computer_cities}")
                exit()
            try:
                cities_set.remove(city)
            except KeyError:
                pprint(f"К сожалению вы ввели неправильный или несуществующий город и проиграли!"
                       f"Вы смогли назвать следующие города: {player_cities}, а компьютер: {computer_cities}")
                exit()
            determining_last_letter(city)
            player_cities.add(city)
            print(f"Вы назвали город {city}")


print(f"Давай сыграем в игру города! Правила у неё довольно простые:")
pprint(rules)
print("Будь внимателен названия городов нужно вводить точно и без знаков препинания и пробелов")

game()

pprint(F"Поздравляю! вы победили сумев назвать все города из нашего списка!"
       F"Вы назвали следующие города: {player_cities}, а компьютер: {computer_cities}")
