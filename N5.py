from colorama import init
import random
init()
from colorama import Fore, Back



numbers = [1, 2, 3, 4]
probabilities = [0.7, 0.2, 0.1, 0.05]
selected_number = random.choices(numbers, weights=probabilities)[0]



uncomone = ['G3SG1 | песчянная буря', 'Nova | Сердечник', 'AUG | Гроза', 'SSG | Голубая хвоя', 'Галиль | Белое напыление']
rare = ['Sawed-Off | Spirit Board', 'Негев | Drop me', 'Mp5-SD | Ликвидация', 'MAC-10 | Заточение', 'SG 553 | Алоха']
epic = ['Рефольвер | Янтарный Шрадиент', 'Tec-9 | Удаленный лоступ', 'FAMAS | Быстрое движение', 'Dual Berettas | Турбодвойники', 'MP7 | Дух бездны']
legendary = ['AWP | Dragon lore', 'M4A4 | Вой', 'Тычковые ножи | африканская сетка', 'Штык-Нож | Водны', 'Нож-бабочка | Волны']


uncomone_int = 0
rare_int = 0
epic_int = 0 
legendary_int = 0
for i in range(20):
    numbers = [1, 2, 3, 4]
    probabilities = [0.7, 0.2, 0.1, 0.05]
    selected_number = random.choices(numbers, weights=probabilities)[0]
    def random_list():
        if selected_number == 1:
            uncomone_random = random.choice(uncomone)
            print(Fore.WHITE + uncomone_random)
            print(' ')
        elif selected_number == 2:
            rare_random = random.choice(rare)
            print(Fore.BLUE + rare_random)
            print(' ')
        elif selected_number == 3:
            epic_random = random.choice(epic)
            print(Fore.MAGENTA + epic_random)
            print(' ')
        else:
            legendary_random = random.choice(legendary)
            print(Fore.YELLOW + legendary_random)
            print(' ')

    def schetchik():
        global uncomone_int, rare_int, epic_int, legendary_int
        if selected_number == 1:
            uncomone_int += 1
        elif selected_number == 2:
            rare_int += 1
        elif selected_number == 3:
            epic_int += 1
        else:
            legendary_int += 1
    random_list()
    schetchik()


if epic_int >= 3:
    print(Back.MAGENTA + "Удача!")
    print(' ')
elif legendary_int >= 1:
    print(Back.YELLOW + "Большая удача!")
    print(' ')
else:
    print(Back.WHITE + 'не повезло :(')
    print(' ')

print(Fore.WHITE + "Обычный: ", uncomone_int)
print(Fore.BLUE + "Редкое: ", rare_int)
print(Fore.MAGENTA + "Эпическое: ", epic_int)
print(Fore.YELLOW + "Легендарное: ", legendary_int)
