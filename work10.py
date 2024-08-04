from Data.marvel import full_dict
from random import randint
from pprint import pprint

marvel_phases = {
        1: 'Первая фаза',
        2: 'Вторая фаза',
        3: 'Третья фаза',
        4: 'Четвертая фаза',
        5: 'Пятая фаза',
        6: 'Шестая фаза'
    }

dict_list = []

films_phase = []

films_phase_simple = []

for key, dict_value in full_dict.items():
    # dict_value["id"] = randint(0, 100000) # присвоение id через библиотеку рандом, я предпочёл в качестве
    # id использовать ключи словаря full_dict, т.к. они идут по порядку.
    dict_value["id"] = key
    dict_list.append(dict_value)

pprint(marvel_phases)

while True:
    try:
        input_phase = input("Введите фазу, фильмы которой вы хотели бы просмотреть:")
        if input_phase.isdigit():
            input_phase = int(input_phase)
        else:
            raise ValueError("ошибка ввода: вы ввели не цифры!")

        if input_phase not in marvel_phases:
            pprint(marvel_phases)
            raise ValueError("К сожалению такой фазы не существует, выберите фазу из списка выше и")
        break
    except ValueError as e:
        print(f"{e} повторите ввод")

while True:
    try:
        output_type = input("Введите тип вывода: 1-простой(название и год), 2-полный")
        if output_type.isdigit():
            output_type = int(output_type)
            if output_type not in [1, 2]:
                raise ValueError("в тип ввода вы должны вводить только 1 или 2")
        else:
            raise ValueError("в тип ввода вы должны вводить только 1 или 2")
        break
    except ValueError as e:
        print(f"{e} повторите ввод")


for film in dict_list:
    phase = marvel_phases[input_phase]
    if film["stage"] == phase:
        films_phase.append(film)
        film_simple = {}
        film_simple["название"] = film["title"]
        film_simple["год"] = film["year"]
        films_phase_simple.append(film_simple)

if output_type == 2:
    pprint(films_phase, sort_dicts=False)
else:
    pprint(films_phase_simple, sort_dicts=False)
