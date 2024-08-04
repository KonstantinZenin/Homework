from statistics import mode
# задача №1

spaceships = [
       ["Falcon", 100000, 10000],
       ["Starblazer", 42000, 12000],
       ["Orion", 330000, 9500]
]
spaceship_speed = 0
spaceship_name = ""
for _ in spaceships:
    if _[2] > spaceship_speed:
        spaceship_speed = _[2]
        spaceship_name = _[0]


print(f"The faster spaceship {spaceship_name} has speed {spaceship_speed} km/h ")

# задача № 2
countries_visited = ["France", "Italy", "Spain", "France", "Italy", "France", "Spain", "Italy"]
most_common_element = mode(countries_visited)
print(most_common_element)

# задача №3

# nums_list_1 = [i for i in range(999)]
nums_list_1 = [1, 9, 50, 21, 6, 8, 1, 44, 0]
max_num = 0
for _ in nums_list_1:
    if _ > max_num:
        max_num = _

print(max_num)
