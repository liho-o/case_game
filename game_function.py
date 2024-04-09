from command_class import Command


def first_stage():
    command_list = []
    for _ in range(4):
        name = input('Введите имя вашей команды\n')
        command = Command(name)
        command_list.append(command)

    return command_list


def round_function():
    not_error = True
    text = 'Введите действие:\n'
    while not_error:
        try:
            action = int(input(text))
            if action in [1, 2, 3, 4, 5]:
                return action
            else:
                text = 'Error\nВы ввели не корретное значение\nВведите действие:\n'
        except ValueError:
            text = 'Error\nВы ввели не корретное значение\nВведите действие:\n'


def command_action(command, action):
    print('Ход команды -', command.name)
    # Добавить оформеление и вывод характеристик команды
    match action:
        case 1:
            command.rocket += 10
        case 2:
            command.science += 10
        case 3:
            command.luck += 10
        case 4:
            pass
            #Запуск рокеты - функция с рандом при успешном запуске записывает  command.success_start = True и конец игры
            #Функция рандома на плохие погодные условия

        case 5:
            pass
            #Анализ данных - увеличивает кратно очки ракеты и ученых сразу ( если были 0 то 0 и остануться)
            #Функция рандома на повреждение бортвого самописца
    print(command.rocket)
    return True


def main_game_stage(command_list):
    for command in command_list:
        command_action(command, round_function())
        if command.success_start:
            return False
    return True


