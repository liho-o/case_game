
class Command:
    def __init__(self, name):
        print('Имя команды -', name)
        # Заменить текст
        self.science = 0
        self.rocket = 0
        self.name = name
        self.exp = 0
        self.success_start = False
        self.failed_fly = 0
