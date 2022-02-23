from .abstract.Actions import Actions
from .controllers.gameController import Bet_1_in_4

class Bet_1_in_4Action(Actions):
    def __init__(self):
        super().__init__(["ลง 1 ใน 4"])

    def do(self, text):
        Bet_1_in_4()