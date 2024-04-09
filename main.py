import game_function

#

if __name__ == "__main__":
    print('***********\nДобро пожаловать в нашу игру "Кто шустрее"\nПрокачайте свои скилы и запустите ракету быстрее соперников\n'
          'Улучшенная ракета и многоопытные инженеры дают наибольшиий шанс на успешный полет\n'
          'Не забывайте, что удача также влияет на успех\nПриятной игры\n***********')
    command_list = game_function.first_stage()
    game_process = True
    while game_process:
        game_process = game_function.main_game_stage(command_list)

