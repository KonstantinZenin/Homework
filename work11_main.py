from Data.cities import cities_list
from pprint import pprint

Rules = (
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

player_score = 0

computer_score = 0

cities_set = {city["name"].lower() for city in cities_list}
# cities_set = {"яхрома", "абаза", "абдулино", "орёл", "лабинск", "калининград"}

cities_used = set()

bad_letters = set()
for city in cities_set:
    last_letter = city[-1]
    for city_2 in cities_set:
        first_letter = city_2[0]
        if last_letter == first_letter:
            break
    else:
        bad_letters.add(last_letter)

city_answer = ""

last_letter_1 = ""
first_letter_1 = ""

while cities_set:
    player_input = input("Введите название города")
    player_city = player_input.lower()
    if player_city == "стоп":
        pprint(f"вы решили прекратить игру, вы проиграли набрав {player_score} очков "
               f"и отгадав следующие города {cities_used}")
    if player_city[0] == last_letter_1 or last_letter_1 == "":
        last_letter_1 = player_city[-1]
        try:
            cities_set.remove(player_city)
        except KeyError:
            print(f"города {player_input} нету в списке играющих городов вы проиграли набрав {player_score} очков "
                  f"и отгадав следующие города {cities_used}")
            exit()
        player_score += 1
        cities_used.add(player_input)
        if last_letter_1 in bad_letters:
            last_letter_1 = player_city[-2]

        # ход компьютера
        first_letter_1 = last_letter_1
        computer_turn_set = {city for city in cities_set if first_letter_1 == city[0]}
        computer_city = computer_turn_set.pop()
        computer_score += 1
        cities_set.remove(computer_city)
        if last_letter_1 in bad_letters:
            last_letter_1 = computer_city[-2]
        pprint(f"Компьютер выбрал город {computer_city.capitalize()} соответственно "
               f"вам нужно назвать город начинающийся на букву \"{last_letter_1}\"")
    else:
        pprint(f"Вы ввели город {player_input}, а он не начинается на букву \"{last_letter_1}\". "
               f"Вы проиграли набрав {player_score} очков и отгадав следующие города {cities_used}")
        exit()

pprint(f"Поздравляю вы отгадали {cities_used} города и победили!")
