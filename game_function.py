from command_class import Command
import random
import lang as ru


def first_stage():
    """
    Naming the teams
    """
    command_list = []
    for _ in range(4):
        name = input(ru.TEAM)
        command = Command(name)
        command_list.append(command)

    return command_list


def round_function(command):
    """
    This function let the players decide on their move
    """
    print(ru.TEAM_MOVE, command.name)
    text = (ru.MOVE)
    while True:
        try:
            action = int(input(text))
            if action in [1, 2, 3, 4, 5]:
                return action
            else:
                text = ru.ERROR_U
        except ValueError:
            text = ru.ERROR_U


def analyse_fly(command):
    """
    If the players choose to analyse their flight their features would multiple
    """
    command.exp += 2 * (command.failed_fly ** 0.5)
    command.rocket *= 1.5
    command.science *= 1.5


def start_rocket(command):
    """
    Testing if the ship will launch
    """
    chance = (command.rocket ** 2 + command.science*2.5 + command.exp ** 1.5)/1000
    i = random.random()
    if chance > i:
        command.success_start = True
        print(ru.VICTORY)
    else:
        print(ru.WEAK)
        command.failed_fly += 1


def random_event():
    """
    An event that players can't influence
    """
    i = random.random()
    if i > 0.3:
        return True
    else:
        return False


def command_action(command, action):
    """
    Benefits that players will gain based on their decision of the move
    """
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
                print(ru.FOG)
        case 5:
            if random_event():
                analyse_fly(command)
            else:
                print(ru.INFO)
    print(ru.SHIP, command.rocket)
    print(ru.SCIENTISTS, command.science)
    print(ru.EXP, command.exp)
    print(ru.FAILED, command.failed_fly)
    return True


def main_game_stage(command_list):
    """
    Detecting if the launch is going to be successful
    """
    for command in command_list:
        command_action(command, round_function(command))
        if command.success_start:
            return False
    return True
