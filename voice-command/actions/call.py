from .abstract.Actions import Actions
from .controllers.gameController import call

class callAction(Actions):
    def __init__(self):
        super().__init__(["คอล", "เช็ค", "ตาม","call","check","ปาล์ม"])

    def do(self, text):
        call()