import game_function



if __name__ == "__main__":
    print('Приветствие')
    command_list = game_function.first_stage()
    game_process = True
    while game_process:
        game_process = game_function.main_game_stage(command_list)

