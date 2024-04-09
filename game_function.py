from data import Command


def first_stage():
    command_list = []
    for _ in range(4):
        name = input('Введите имя вашей команды\n')
        command = Command(name)
        command_list.append(command)

    # for command in command_list:
    #     print(command.name)


def round_function():
    not_error = True
    text = 'Введите действие:\n'
    while not_error:
        try:
            action = int(input(text))
            if action in [1, 2, 3, 4]:
                return action
        except ValueError:
            text = 'Error\nВы ввели не корретное значение\nВведите действие:\n'


def command_action(command, action):
    match action:
        case 1:
            command.rocket += 10
    print(command.rocket)


def main_game_stage(command_list):
    for command in command_list:
        round_function(command)
