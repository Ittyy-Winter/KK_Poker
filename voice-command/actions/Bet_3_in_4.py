from .abstract.Actions import Actions
from .controllers.gameController import Bet_3_in_4

class Bet_3_in_4Action(Actions):
    def __init__(self):
        super().__init__(["ลง 3 ใน 4", "ลง 3 ส่วน 4"])

    def do(self, text):
        Bet_3_in_4()