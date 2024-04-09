import game_function
import data
game_process = True


if __name__ == "__main__":
    print('Приветствие')
    # game_function.first_stage()
    while game_process:
        a = data.Command('test')
        action = game_function.round_function()
        game_function.command_action(a, action)
        game_process = False

