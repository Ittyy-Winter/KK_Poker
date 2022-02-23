from .abstract.Actions import Actions
from .controllers.gameController import fold

class foldAction(Actions):
    def __init__(self):
        super().__init__(["หมอบ", "ไม่เล่น", "ขอผ่าน","fold"])

    def do(self, text):
        fold()