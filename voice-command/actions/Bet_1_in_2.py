from .abstract.Actions import Actions
from .controllers.gameController import Bet_1_in_2

class Bet_1_in_2Action(Actions):
    def __init__(self):
        super().__init__(["ลง 1 ใน 2", "half bet", "ลงหนึ่งในสอง"])

    def do(self, text):
        Bet_1_in_2()
