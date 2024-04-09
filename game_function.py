from command_class import Command
import random


def first_stage():
    command_list = []
    for _ in range(4):
        name = input('Введите название вашей команды\n')
        command = Command(name)
        command_list.append(command)

    return command_list


def round_function(command):
    print('----------------\nХод команды -', command.name)
    text = ('Выберите действие:\n1 - модернизировать ракету\n2 - прокачать ученых\n3 - увеличить опыт инженеров\n'
            '4 - полететь!!!\n5 - анализ неудачных полетов\n')
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
    command.exp += 2*(command.failed_fly)**0.5
    command.rocket *= 1.5
    command.science *= 1.5


def start_rocket(command):
    chance = (command.rocket ** 2 + command.science*2.5 + command.exp ** 1.5)/1000
    i = random.random()
    if chance > i:
        command.success_start = True
        print('---Поздравляем! Ваша ракета успешно взлетела! Вы победили!---')
    else:
        print("---Ваша ракета не взлетела. Прокачайте ее лучше---")
        command.failed_fly += 1



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
                print('---Полет отменен - плохая видимость из-за сильного тумана(---')
        case 5:
            if random_event():
                analyse_fly(command)
            else:
                print('---Не повезло - повредился бортовой самописец. Информация о полете не сохранилась')
    print('Ракета -', command.rocket)
    print('Ученые -', command.science)
    print('Опыт -', command.exp)
    print('Количество неудачных попыток -', command.failed_fly)
    return True


def main_game_stage(command_list):
    for command in command_list:
        command_action(command, round_function(command))
        if command.success_start:
            return False
    return True
