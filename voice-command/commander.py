from actions.call import callAction
from actions.fold import foldAction
from actions.Bet_1_in_2 import Bet_1_in_2Action
from actions.Bet_1_in_4 import Bet_1_in_4Action
from actions.Bet_3_in_4 import Bet_3_in_4Action
from actions.Bet_All_in import Bet_All_inAction
from actions.Bet_Min import Bet_MinAction


def matchAction(text, actions):
    orders = []

    for action in actions:
        isMatch, word = action.isMatch(text)

        if not isMatch:
            continue

        idx = text.lower().index(word.lower())
        if idx > -1:
            orders.append({
                "action": action,
                "idx": idx
            })

    orders.sort(key=lambda x: x["idx"])
    return orders

def contextSelection(text):
    actions = [
        callAction(),
        foldAction(),
        Bet_1_in_2Action(),
        Bet_1_in_4Action(),
        Bet_3_in_4Action(),
        Bet_All_inAction(),
        Bet_MinAction()
    ]
    orders = matchAction(text, actions)

    for i in range(len(orders)):
        order = orders[i]
        endContext = len(text)

        if i < len(orders) - 1:
            endContext = orders[i+1]["idx"]

        currentContext = text[order["idx"]:endContext]
        order["action"].do(currentContext)