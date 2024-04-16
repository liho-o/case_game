
class Command:
    def __init__(self, name):
        '''
        Features that determine  if the ship will launch
        '''
        print('Имя команды -', name)
        self.science = 0
        self.rocket = 0
        self.name = name
        self.exp = 0
        self.success_start = False
        self.failed_fly = 0
