
class Command:

    def __init__(self, name):
        print('Имя команды -', name)
        self.science = 0
        self.rocket = 0
        self.name = name
        self.luck = 0
        self.success_start = False
