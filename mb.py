class Game(object):
""""сама игра(типо посредник между игроками)"""
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    field_size = len(letters)

    def __init__(self):

        self.players = []
        self.current_player = None
        self.next_player = None
        self.status = 'prepare'
class BasePlayer():
    """"игроки (их бэйсик умения)"""
    def __init__(self, make_shot, build_field,receive_shot):
        self.make_shot = make_shot
        self.build_field = build_field
        self.receive_shot = receive_shot
class AI_Player(BasePlayer):
    """"типо ии хз"""
    def __init__(self, my_field, enemy_field, placement_stretess):
        """я плаки плаки, ничего не понимаю(( спасите, пожалуйста"""


class Huamen_Player(BasePlayer):
    """"ну мыыы"""
    def __init__(self, my_field, enemy_field, build_fild, receive_shot):
        """все еще ничего не понимаю..."""


