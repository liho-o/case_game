from command_class import Command
import random


def first_stage():
    command_list = []
    for _ in range(4):
        name = input('Введите имя вашей команды\n')
        command = Command(name)
        command_list.append(command)

    return command_list


def round_function(command):
    print('Ход команды -', command.name)
    # Добавить оформление и вывод характеристик команды
    text = 'Введите действие:\n'
    # Расписать текст
    while True:
        try:
            action = int(input(text))
            if action in [1, 2, 3, 4, 5]:
                return action
            else:
                text = 'Error\nВы ввели не корретное значение\nВведите действие:\n'
        except ValueError:
            text = 'Error\nВы ввели не корретное значение\nВведите действие:\n'


def analyse_fly(command):
    command.science *= 1.5
    command.rocket *= 1.3
    # Анализ данных - увеличивает кратно очки ракеты и ученых сразу ( если были 0 то 0 и остануться)


def start_rocket(command):
    # Запуск ракеты - функция с рандом при успешном запуске
    # записывает  command.success_start = True и конец игры
    chance = (command.rocket ** 2 + command.science*2.5 + command.exp ** 1.5)/1000
    i = random.random()
    if chance > i:
        command.success_start = True
    else:
        print("Плохая попытка")



def random_event():
    i = random.random()
    if i > 0.3:
        return True
    else:
        return False


def command_action(command, action):

    match action:
        case 1:
            command.rocket += 10
        case 2:
            command.science += 10
        case 3:
            command.exp += 10
        case 4:
            if random_event():
                start_rocket(command)
            else:
                print('Неудача - погода')
                # Заменить текст
        case 5:
            if random_event():
                analyse_fly(command)
            else:
                print('Неудача - повреждение бортвого самописца')
                # Заменить текст
    print('Ракета -',command.rocket)
    print('Ученые -', command.science)
    print('Опыт -', command.exp)

    return True


def main_game_stage(command_list):
    for command in command_list:
        command_action(command, round_function(command))
        if command.success_start:
            return False
    return True
