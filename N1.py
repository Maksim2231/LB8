import random

s = ["Михаил", "София", "Париж", "Андрей", "Ольга", "Барселона", "Лев", "Блондин", "Чтение", "Архитектор", "Мюнхен", "Наталья", "Амстердам", "Кошка", 
     "Йога", "Художник", "Лондон", "Алексей", "Токио", "Волк", "Катание на коньках", "Учитель", "Берлин", "Виктория", "Мадрид", 
     "Попугай", "Пение", "Программист", "Рим", "Даниил", "Нью-Йорк", "Гепард", "Фотография", "Инженер", "Мария", "Чикаго", "Змея", "Брюнет", "Гитара", "Лётчик", "Москва", 
     "Иван", "Дубай", "Слон", "Рисование", "Адвокат", "Милан", "Елена", "Сидней", "Лиса", "Бег", "Дизайнер", "Амстердам", "Павел", "Канкун", "Панда", "Скейтбординг", 
     "Фотограф", "Венеция", "Анна", "Мумбаи", "Кролик", "Бег", "Дизайнер", "Каир", "Анастасия", "Торонто", "Обезьяна", "Танцы", "Бухгалтер", "Лас-Вегас", "Екатерина", 
     "Шанхай", "Гепард", "Лыжи", "Биолог", "Стамбул", "Дмитрий", "Хельсинки", "Жираф", "Танцы живота", "Стоматолог", "Афины", "Ева"]

questions = ['Как тебя зовут?', 'Где ты живешь?', 'Каким спортом ты занимаешься?', 'Какое у тебя хобби?', 'Какое у тебя домашнее животное?', 'Где ты хочешь побывать?', 'Какая твоя профессия?', 'Какое твое любимое блюдо?',
             'Кто ты по жизни?', 'Какое дикое животное тебе подходит?']


player_history = []
pc_history = []

current_index = 0
current_index2 = 0

def catch_ball():
    if random.random() <= 0.3:
        return True
    else:
        return False

def playing_game(current_index):
    for i in range(1, 11):
        if catch_ball():
            print('Компьютер бросил мяч, Вы поймали!')
            quest = questions[current_index]
            print('Вопрос: ', quest)
            answer = input('Введите ответ: ')
            print('Ответ: ', answer)
            print(' ')
            player_history.append(answer)
            current_index += i
        else:
            print('Компьютер бросил мяч, Вы НЕ поймали!')
            quest = questions[current_index]
            print('Вопрос: ', quest)
            answer = random.choice(s)
            print('Ответ: ', answer)
            print(' ')
            player_history.append(answer)
            current_index += i

playing_game(current_index)

print('--------------------------------------------------------')
print('Рассказ меня: ')
print('Меня зовут', player_history[0], 'я живу в', player_history[1], 'я занимаюсь', player_history[2], 'мое хобби это', player_history[3], 'мое домашнее животное это', 
      player_history[4], 'я хочу побывать в', player_history[5], 'моя профессия это', player_history[6], 'мое любимое блюдо', player_history[7], 'я по жизни', player_history[8], 
      'мне подходит', player_history[9])
print('--------------------------------------------------------')
print(' ')

def playing_player_comp(current_index2):
    for r in range(1, 11):
        if catch_ball():
            print('Вы бросили мяч, Комп поймал!') 
            quest = questions[current_index2]
            print('Вопрос: ', quest)
            answer = random.choice(s)
            print('Ответ: ', answer)
            print(' ')
            pc_history.append(answer)
            current_index2 += r
        else:
            print('Вы бросили мяч, Комп НЕ поймал!')
            quest = questions[current_index2]
            print('Вопрос: ', quest)
            answer = input('Введите ответ: ')
            print('Ответ: ', answer)
            print(' ')
            pc_history.append(answer)
            current_index2 += r

playing_player_comp(current_index2)


print('--------------------------------------------------------')
print('Рассказ ПК: ')
print('Меня зовут', pc_history[0], 'я живу в', pc_history[1], 'я занимаюсь', pc_history[2], 'мое хобби это', pc_history[3], 'мое домашнее животное это', 
      pc_history[4], 'я хочу побывать в', pc_history[5], 'моя профессия это', pc_history[6], 'мое любимое блюдо', pc_history[7], 'я по жизни', pc_history[8], 
      'мне подходит', pc_history[9])
print('--------------------------------------------------------') 
