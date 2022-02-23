from .abstract.Actions import Actions
from .controllers.gameController import Bet_All_in

class Bet_All_inAction(Actions):
    def __init__(self):
        super().__init__(["หมดหน้าตัก","ทุ่มหมดตัว", "All in"])

    def do(self, text):
        Bet_All_in()