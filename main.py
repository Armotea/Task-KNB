print("""Игра "Камень, ножницы, бумага"
Правила игры: вам нужно выбрать число, соответствующее знаку,
который вы хотите использовать в игре!
1 - Камень, 2 - Бумага, 3 - Ножницы
Камень побеждает ножницы; Бумага побеждает камень; Ножницы побеждают бумагу.
""")

tim_choice = int(input("Знак выбирает Тимур: "))
rus_choice = int(input("Знак выбирает Руслан: "))

if ((tim_choice > 3) or (tim_choice < 1)) or ((rus_choice > 3) or (rus_choice < 1)):
    print("Вы ввели некорректное значение!!!")

if tim_choice == 1 and rus_choice == 3:
    print("Победил Тимур!!!")
elif tim_choice == 2 and rus_choice == 1:
    print("Победил Тимур!!!")
elif tim_choice == 3 and rus_choice == 2:
    print("Победил Тимур!!!")
elif tim_choice == rus_choice:
    print("Ничья!!!")
else:
    print("Победил Руслан!!!")