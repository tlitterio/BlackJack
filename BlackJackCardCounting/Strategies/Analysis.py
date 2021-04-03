import Logging.LogInput
import TableHelpers
from Strategies import Standard
import Strategies.Standard
from settings import debug
import settings

def PlayRound(player,round):
    id = 999
    if debug == 1:Logging.LogInput.Log(id,
                         TableHelpers.round,
                         "Playing Round: {}"
                         .format(TableHelpers.round))
    while (OpenHands(player) != 0):
        for hand in player._hands:
            while (hand._closed != 1): 
                hand = AnalyzeHand(hand)
                if ("Split" in hand._results[len(hand._results)-1]):
                    player = TableHelpers.Split(player,hand)
            else: continue
    return player

def AnalyzeHand(hand):
    id = 1000
    if debug == 1:Logging.LogInput.Log(id,
                         TableHelpers.round,
                         "Starting Analyzing Hand")
    hand._iteration += 1
    test = len(hand._cards)
    hand = TableHelpers.ScoreKeeper(hand)
    dvcv = settings.dealersvisiblecardvalue
    lastResult = ""
    #while (hand._closed != 1 or lastResult != "Split"):
    hand = Strategies.Standard.StandardMethod(hand)
    if (hand._results != []):
        lastResult = hand._results[len(hand._results)-1]
    if ("Stand" in lastResult 
        or "Busted" in lastResult
        or "BlackJack" in lastResult
        or "DealerBlackJack" in lastResult):
        if debug == 1:Logging.LogInput.Log(id,
                             TableHelpers.round,
                             "Stand in LastResult; {}"
                             .format(lastResult,lastResult))
        hand._closed = 1
        return hand
    elif ("Double" in lastResult):
        if debug == 1:Logging.LogInput.Log(id,
                             TableHelpers.round,
                             "Double in LastResult; Doubling Down"
                             .format(lastResult))
        hand = TableHelpers.Hit(hand)
        hand._closed = 1
        return hand
    elif ("Hit" in lastResult):
        if debug == 1:Logging.LogInput.Log(id,
                             TableHelpers.round,
                             "Hit in LastResult; Hitting"
                             .format(lastResult))
        hand = TableHelpers.Hit(hand)
        return hand
    elif ("Split" in lastResult):
        if debug == 1:Logging.LogInput.Log(id,
                             TableHelpers.round,
                             "Split in LastResult; Spliting"
                             .format(lastResult))
        return hand
    else:
        if debug == 1:Logging.LogInput.Log(id,
                             TableHelpers.round,
                             "     Something Wrong")
        return hand
    lastResult = hand._results[len(hand._results)-1]
def OpenHands(player):
    id = 33
    if debug == 1:Logging.LogInput.Log(id,TableHelpers.round,"Checking for Open Hands")
    count =0
    for h in player._hands:
        if h._closed == 0:
            count +=1
    return count