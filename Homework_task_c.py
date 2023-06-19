from itertools import zip_longest

# Задание
# на вход 2 списка: автомобили и имена
# подобрать автомобиль владельцу по алфавитному порядку
# если не одинаковы по длине, сообщить что автомобиль не достанется

# решение 1
# from itertools import zip_longest
# names = ["Sofia Goggia", "Mikaela Shiffrin", "Wendy Holdener", "Lindsey Vonn", "Frida Hansdotter", "Michelle Gisin",
#          "Ragnhild Mowinckel", "Federica Brignone", "Tina Weirather", "Ester Ledecka"]
# cars = ["Porche", "Lada", "Ferrari", "Lexus", "Cadillac", "Bentley", "Lamborghini", "Bugatti", "Audi"]
# names.sort()
# longest = range(len(names))
# names_cars = zip_longest(names, cars, longest, fillvalue="Нет машины")
# print(list(names_cars))


# решение 2
names = ["Sofia Goggia", "Mikaela Shiffrin", "Wendy Holdener", "Lindsey Vonn", "Frida Hansdotter", "Michelle Gisin",
         "Ragnhild Mowinckel", "Federica Brignone", "Tina Weirather", "Ester Ledecka"]
cars = ["Porche", "Lada", "Ferrari", "Lexus", "Cadillac", "Bentley", "Lamborghini", "Bugatti", "Audi"]
cars.sort()
names.sort()
names_cars = list(zip_longest(names, cars, fillvalue="Нет машины"))
new_names_cars = {i[0]:i[1] for i in names_cars}
print(new_names_cars)
