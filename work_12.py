from Data.marvel import full_dict
from pprint import pprint

user_input: list = list(map(lambda stringify: int(stringify) if stringify.isdigit() else None,
                            input("введите id фильмов через пробел").split(" ")))
pprint(f"Вы ввели следующие id:{user_input}", sort_dicts=False)

print("_____________________________________________________________________________________________")

filtered_list_of_dicts = []

for id, film_data in filter(lambda film_id: film_id[0] in user_input, full_dict.items()):
    new_dict = {"id": id, **film_data}
    filtered_list_of_dicts.append(new_dict)

pprint(f"По ним мы нашли фильмы:{filtered_list_of_dicts} ", sort_dicts=False)

print("_____________________________________________________________________________________________")

director_set = {director["director"] for director in filtered_list_of_dicts}

pprint(f"Их режиссировали: {director_set}", sort_dicts=False)

print("_____________________________________________________________________________________________")

year_to_str_dict = {key: {**value, 'year': str(value['year'])} for key, value in full_dict.items()}

pprint(f"В этом словаре мы изменили значение года с числа на строку. {year_to_str_dict}", sort_dicts=False)

print("_____________________________________________________________________________________________")

dict_filtered_by_letter = dict(filter(lambda x: x[1]['title'][0].strip().lower() == 'ч',
                                     filter(lambda x: x[1]['title'] is not None, full_dict.items())))

pprint(f"В этом словаре находятся только фильмы начинающиеся"
       f" на букву \"ч\" {dict_filtered_by_letter}", sort_dicts=False)

print("_____________________________________________________________________________________________")

film_sorted_by_year = dict(sorted(full_dict.items(), key=lambda x: x[1]['year'] if isinstance(x[1]['year'],
                                                                                              int) else False))
pprint(f"Фильмы отсортированные по году:{film_sorted_by_year}", sort_dicts=False)
