import re
password = "zxcedv+"
password_regexp_lvl1 = r".{8,}"
password_regexp_lvl2 = r"\d+"
password_regexp_lvl3 = r"[a-zа-я]+"
password_regexp_lvl4 = r"[A-ZА-Я]+"
password_regexp_lvl5 = r"[\W]"
password_strength = 0
conclusion = ""

while True:

    if re.search(password_regexp_lvl1, password) != None:
        password_strength += 1

    if re.search(password_regexp_lvl2, password) != None:
        password_strength += 1

    if re.search(password_regexp_lvl3, password) != None:
        password_strength += 1

    if re.search(password_regexp_lvl4, password) != None:
        password_strength += 1

    if re.search(password_regexp_lvl5, password) != None:
        password_strength += 1
    break

if password_strength == 2:
    if re.search(password_regexp_lvl4, password) != None and re.search(password_regexp_lvl3, password) != None:
        password_strength = 2


if password_strength == 0:
    print("Пароль должен состоять как минимум из 8 символов")
elif password_strength == 1:
    conclusion = "Вы ввели самый лёгкий пароль."
elif password_strength == 2:
    conclusion = "Вы ввели лёгкий пароль."
elif password_strength == 3:
    conclusion = "Вы ввели пароль средней сложности."
elif password_strength == 4:
    conclusion = "Вы ввели сложный пароль."
elif password_strength == 5:
    conclusion = "Вы ввели самый сложный пароль."

print(conclusion)
