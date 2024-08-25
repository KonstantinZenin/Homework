import json

from Data.cities import cities_list
from pprint import pprint
from random import randint

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

json_file = "./data/cities.json"

player_input = ""

player_score = 0

computer_score = 0


# cities_set = {city["name"].lower() for city in cities_list}
# cities_set = {"яхрома", "абаза", "абдулино", "орёл", "лабинск", "калининград", "вад"}

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(cities_list, file, ensure_ascii=False, indent=4)

with open(json_file, "r", encoding="utf-8") as file:
    cities_list_from_fson = json.load(file)

cities_set = {city["name"].lower() for city in cities_list_from_fson}

print(cities_set)

player_cities = set()

computer_cities = set()

bad_letters = set()

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


def last_letter_determining(city):
    global last_letter_1
    indent = -1
    if city[-1] in bad_letters:
        indent -= 1
        last_letter_1 = city[indent]
    else:
        last_letter_1 = city[indent]


def first_turn_determining():
    first_turn = randint(0, 10)
    return first_turn


def find_cities_help():
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


def player_turn():
    name = "игрок"
    help_1 = find_cities_help()
    pprint(help_1)
    player_input = input("Введите название города")
    city = player_input.lower()
    turn = 0
    return city, name, turn


def computer_turn():
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
    global turn
    if turn == 200:
        turn = first_turn_determining()

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
            last_letter_determining(city)
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
            last_letter_determining(city)
            player_cities.add(city)
            print(f"Вы назвали город {city}")


print(f"Давай сыграем в игру города! Правила у неё довольно простые:")
pprint(rules)
print("Будь внимателен названия городов нужно вводить точно и без знаков препинания и пробелов")
game()

game()

pprint(F"Поздравляю! вы победили сумев назвать все города из нашего списка!"
       F"Вы назвали следующие города: {player_cities}, а компьютер: {computer_cities}")
