from .abstract.Actions import Actions
from .controllers.gameController import Bet_Min

class Bet_MinAction(Actions):
    def __init__(self):
        super().__init__(["ลงต่ำ","ลงขั้นต่ำ"])

    def do(self, text):
        Bet_Min()