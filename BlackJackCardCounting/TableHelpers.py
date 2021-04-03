import Classes.Players
#import Classes.Shoe
import Classes.Cards
import Classes.Hands
import settings
from imp import reload
import Logging.LogInput
import sys
from settings import *

def InitializePlayers():
    global numberOfPlayers
    players = []
    id = 1
    if debug == 1:Logging.LogInput.Log(id,settings.round,"Initializing Players",)
    if (numberOfPlayers == 0): 
        numberOfPlayers = 2
    playerCounter = numberOfPlayers
    active = 1
    while len(players) < playerCounter:

        if (len(players) == 0): 
            label = "Counter"
            active = 1
            if debug == 1:Logging.LogInput.Log(id,round,"     Defining Counter")
        elif (len(players) == 1 and numberOfPlayers > 2): 
            label = "MoneyBags"
            purse = MaximumBet*10
            active = 0
            if debug == 1:Logging.LogInput.Log(id,round,"     Defining Money Bags")
        elif (len(players) == numberOfPlayers-1): 
            label = "Dealer"
            active = 1
            if debug == 1:Logging.LogInput.Log(id,round,"     Defining Dealer")
        else: 
            label = "Player"
            if debug == 1:Logging.LogInput.Log(id,round,"     Defining General Player")
        tempPlayer = Classes.Players.Player(label,len(players),active)
        players.append(tempPlayer)
    return players
    if debug == 1:Logging.LogInput.Log(id,round,"Returning Initialized Players")
def InitializeShoe():
    reload(settings)
    id = 2
    #global cardsFaceValues
    #global cardsSuitValues
    #global discarded
    shoe = settings.shoe
    shoe._simulationId = settings.SimulationId
    if debug == 1:Logging.LogInput.Log(id,round,"Initializing Shoe")
    try:
        if (len(shoe._cards) == 0): 
            shoe = FillShoe(shoe)
        while (len(settings.discarded) >0) :
            TempCard = settings.discarded.pop(0)
            TempCard._initallyhidden = 0
            if (TempCard._cardFace == "Ace"):
                TempCard._value = 11
            settings.shoe._cards.append(TempCard)
        settings.shoe = Shuffle(settings.shoe)
        return
    except:
        e = sys.exc_info()[0]
        if debug == 1:Logging.LogInput.Log(id,e,round)
    if debug == 1:Logging.LogInput.Log(id,round,"Storing Filled & Shuffled Shoe")
def FillShoe(shoe):
    id = 2
    if debug == 1:Logging.LogInput.Log(id,round,"Filling Shoe")
    try:
        d=decks
        c=cardsFaceValues
        s=cardsSuitValues
        cf=""
        sf=""
        ind =0
        while (d > 0):
            s=cardsSuitValues
            while (s > 0):
                #region Label Suit
                if (s==4): sf="Spades"
                elif (s==3): sf="Hearts"
                elif (s==2): sf="Clubs"
                elif (s==1): sf="Diamonds"
                #endregion
                c=cardsFaceValues
                while (c > 1):
                    #region Label Face
                    if (c==14): cf="Ace";v=11
                    elif (c==13): cf="King";v=10
                    elif (c==12): cf="Queen";v=10
                    elif (c==11): cf="Jack";v=10
                    elif (c==10): cf="Ten";v=10
                    elif (c==9): cf="Nine";v=9
                    elif (c==8): cf="Eight";v=8
                    elif (c==7): cf="Seven";v=7
                    elif (c==6): cf="Six";v=6
                    elif (c==5): cf="Five";v=5
                    elif (c==4): cf="Four";v=4
                    elif (c==3): cf="Three";v=3
                    elif (c==2): cf="Two";v=2
                    #endregion
                    Temp = Classes.Cards.Card(ind,d,v,cf,s,sf)
                    shoe._cards.append(Temp)
                    ind+=1
                    c-=1
                s-=1
            d-=1
    except:
        e = sys.exc_info()[0]
        if debug == 1:Logging.LogInput.Log(id,e,round)
    if debug == 1:Logging.LogInput.Log(id,round,"Returning Filled Shoe")
    return shoe
def Shuffle(shoe):
    id = 4
    #global round
    #global shoe
    cards = settings.shoe._cards
    from random import shuffle
    if debug == 1:Logging.LogInput.Log(id,round,"Shuffling Shoe")
    try:
        shuffle(cards)
        shuffle(cards)
        shuffle(cards)
    except:
        e = sys.exc_info()[0]
        if debug == 1:Logging.LogInput.Log(id,e,round)
    if debug == 1:Logging.LogInput.Log(id,round,"Returning Shuffled Shoe")
    return shoe
def ResetShoe():
    #settings.shoe
    id = 8000
    if (len(settings.shoe._cards) == 0): 
        FillShoe()
    if (len(settings.shoe._cards)/fullDecklength < reshufflePercentage):
        print("Reshuffling.......")
        if debug == 1:Logging.LogInput.Log(id,round,"Reshuffling.......")
        while (len(settings.discarded) > 0) :
            TempCard = settings.discarded.pop(0)
            if (TempCard._cardFace == "Ace"):
                TempCard._value = 11
            settings.shoe._cards.append(TempCard)
        for p in players:
            p._cbet = p._ibet
        settings.shoe = Shuffle(settings.shoe)
        settings.shoe._totalcount = 0
        settings.shoe._percentagecount = 0
def DealHand():
    id = 200
    if debug == 1:Logging.LogInput.Log(id,round,"Dealing Hand")
    deal = 2
    while deal > 0:
        for p in settings.players:
            if p._hands == []: 
                tempHand = Classes.Hands.Hand()
                p._hands.append(tempHand)
            for h in p._hands:
                tempCard = settings.shoe._cards.pop(0)
                h._cards.append(tempCard)
                if (tempCard._cardFace == "Ace"):
                    h._bigaces += 1
                if (p._label ==  "Dealer"):
                    h._dealer = 1
                    if (deal == 2): 
                        settings.dealersvisiblecardvalue = tempCard._value
                if (deal == 2): 
                    h._results.append("First Card")
                settings.discarded.append(tempCard)
        deal -= 1
    for p in players:
        for h in p._hands:
            ScoreKeeper(h)
def ClearRound():
    id = -99
    #global players
    if debug == 1:Logging.LogInput.Log(id,round,"Round Complete - Clear Round")
    for p in settings.players:
        p._hands = []
    settings.shoe._roundcount = 0

def ScoreKeeper(hand):
    id = 2000
    #global dealersvisiblecardvalue
    #global dealersScore
    if (hand._score < 4 and hand._score != 0):
        test = 4
    hand._hand = []
    if debug == 1:Logging.LogInput.Log(id,round,"Executing ScoreKepper Method")
    if hand._bigaces > 1:
        test = 0
    def CalculateHand(hand):
        TempScore = 0
        bigaces = 0
        littleaces = 0
        cardsinhand = 0
        counter = 0
        handarray = []
        for c in hand._cards:
            if (c._value ==  11): 
                bigaces += 1
            if (c._value == 1): 
                littleaces += 1
            TempScore += c._value
            handarray.append(c._value)
            counter += 1
        hand._cardsinhand = counter
        hand._bigaces = bigaces
        hand._littleaces = littleaces
        hand._score = TempScore
        hand._hand = handarray
        list.sort(hand._hand)
        return hand
    if ((len(hand._cards) == 2)
        and (hand._cards[0]._cardFace == hand._cards[1]._cardFace)):
        if (hand._cards[0]._cardFace == "Ace"):
            hand._duplicate = 11
        else:
            hand._duplicate = hand._cards[0]._value
    hand = CalculateHand(hand)
    while (hand._score > 21 and hand._bigaces > 0):
        for c in hand._cards:
            if (c._value == 11):
                c._value = 1
                hand._bigaces -= 1
                hand._littleaces += 1
                hand = CalculateHand(hand)
                break
            else:
                continue
    if hand._dealer == 1:
        settings.dealersvisiblecardvalue = hand._cards[0]._value
        if (settings.dealersvisiblecardvalue == 1): 
            settings.dealersvisiblecardvalue =11
        settings.dealersScore = hand._score
    if debug == 1:Logging.LogInput.Log(id,round,"Returning Scored Round")
    if (hand._score < 4 and hand._score != 0):
        test = 4
    return hand

def Hit(hand):
    TempCard = settings.shoe._cards.pop(0)
    hand._cards.append(TempCard)
    settings.discarded.append(TempCard)
    if TempCard._value == 11: 
        hand._bigaces += 1
    hand._hand.append(TempCard._value)
    hand = ScoreKeeper(hand)
    if (hand._results != [] 
        and "Double" in hand._results[len(hand._results)-1]):
        hand._results.append("Hitting on Double")
    return hand

def Split(player,hand):
    id = 3000
    handStr =""
    for i in hand._hand:
        handStr += str(i)
        handStr += ","
    if debug == 1:Logging.LogInput.Log(id,
                         round,
                         "Executing Split Action: {} - {}"
                         .format(handStr,dealersvisiblecardvalue))
    oldhand = hand
    oldhandid = player._hands.index(hand)
    for c in oldhand._cards:
        if c._cardFace == "Ace":
            c._value = 11
    splitCard = oldhand._cards.pop()
    splitCard._parent = oldhandid
    newhand = Classes.Hands.Hand()
    newhand._cards.append(splitCard)
    oldhand = Hit(oldhand)
    newhand = Hit(newhand)

    oldhand._split = 1
    newhand._split = 1
    oldhand._results = []
    oldhand._results.append("First Card From Split (Old Hand)")
    newhand._results = []
    newhand._results.append("First Card From Split (New Hand)")
    oldhand._closed = 0
    newhand._closed = 0
    oldhand._sibling = oldhandid
    newhand._sibling = oldhandid
    oldhand = ScoreKeeper(oldhand)
    newhand = ScoreKeeper(newhand)
    player._hands[oldhandid] = oldhand
    player._hands.append(newhand)
    for h in player._hands:
        handStr = ''.join(str(e) for e in hand._hand)
        if debug == 1:Logging.LogInput.Log(id,
                             round,
                             "Returning Hand from Split: {} - {}"
                             .format(handStr,dealersvisiblecardvalue))
    if debug == 1:Logging.LogInput.Log(id,
                         round,
                         "Returning Player from Split")
    return player
    test =0

def ScoreRound():
    id = 950
    if debug == 1:Logging.LogInput.Log(id,round,"Scoring Round")
    for p in settings.players:
        for hand in p._hands:
            if (p._label == "Dealer"):
                hand._result = None
                return
            lastresultaction = hand._results[len(hand._results)-1]

            if (hand._score > 21 or (hand._score < settings.dealersScore and settings.dealersScore <= 21)):
                if ("Double" in lastresultaction):
                    hand._result = "LoseDouble"
                else: hand._result = "Lose"

            elif (hand._score == settings.dealersScore and hand._score <= 21):
                hand._result = "Push"

            elif ((hand._score > settings.dealersScore and hand._score <= 21) 
                  or (settings.dealersScore > 21 and hand._score <= 21)):
                if (hand._score == 21 
                    and len(hand._cards) == 2 
                    and hand._split == 0):
                    hand._result = "BlackJack"
                elif ("Double" in lastresultaction):
                    hand._result = "WinDouble"
                else: 
                    hand._result = "Win"
            else:
                hand._result = "ERROR - ScoreRound"   
            if debug == 1:Logging.LogInput.Log(id,round,"Result of Scoring Round for Player {}: {}".format(p._label,hand._result))
def CalculatePayouts():
    if (settings.shoe._percentagecount > 5):
        test=0
    id = 10000000
    if debug == 1:Logging.LogInput.Log(id,settings.round,"Calculating Payouts")
    for p in settings.players:
        if (p._label == "Dealer"):
            return
        else:
            if (settings.shoe._percentagecount >= .05 and settings.shoe._percentagecount < .07):
                    p._cbet = tableminimumbet*10
            elif (settings.shoe._percentagecount >= .07):
                if (settings.shoe._percentagecount <.1):
                    p._cbet = tableminimumbet*20
                elif (settings.shoe._percentagecount <.125 
                      and p._purse < WalkAwayWinLimit):
                    p._cbet = tableminimumbet*30
                elif (settings.shoe._percentagecount <.125 
                      and p._purse > WalkAwayWinLimit):
                    p._cbet = tablemaximumbet
                elif (settings.shoe._percentagecount >= .15 
                      and p._purse > WalkAwayWinBigLimit):
                    p._cbet = tablemaximumbet
                elif (settings.shoe._percentagecount >= .15 
                      and p._purse < WalkAwayWinBigLimit 
                      and p._purse > WalkAwayWinLimit):
                    p._cbet = tablemaximumbet
            else:
                p._ibet = tableminimumbet
                p._cbet = p._ibet
            for h in p._hands:
                op = p._purse
                if (h._result == "BlackJack"):
                    p._lastroundpayout = p._cbet*blackjackpayout
                    p._purse += p._lastroundpayout
                    if debug == 1:Logging.LogInput.Log(
                        id,
                        round,
                        "BlackJack Payout: {} "
                        "Player Score: {} "
                        "Dealer Score: {} "
                        "old purse: {} "
                        "New Purse: {} "
                        "Current Bet Amount: {}"
                        .format(
                            p._cbet*blackjackpayout,
                            h._score,
                            settings.dealersScore,
                            op,
                            p._purse,
                            p._cbet
                            )
                        )
                elif (h._result == "WinDouble"):
                        p._lastroundpayout = p._cbet*2
                        p._purse += p._lastroundpayout
                        if debug == 1:Logging.LogInput.Log(
                            id,
                            round,
                            "Double Payout: {} "
                            "Player Score: {} "
                            "Dealer Score: {} "
                            "old purse: {} "
                            "New Purse: {} "
                            "Current Bet Amount: {}"
                            .format(
                                p._cbet*2,
                                h._score,
                                settings.dealersScore,
                                op,
                                p._purse,
                                p._cbet
                                )
                            )
                elif (h._result == "LoseDouble"):
                        p._lastroundpayout = p._cbet*2
                        p._purse -= p._lastroundpayout
                        if debug == 1:Logging.LogInput.Log(
                            id,
                            round,
                            "Double Lose: {} "
                            "Player Score: {} "
                            "Dealer Score: {} "
                            "old purse: {} "
                            "New Purse: {} "
                            "Current Bet Amount: {}"
                            .format(
                                p._cbet*2,
                                h._score,
                                settings.dealersScore,
                                op,
                                p._purse,
                                p._cbet
                                )
                            )
                elif (h._result == "Win"):
                        p._lastroundpayout = p._cbet
                        p._purse += p._lastroundpayout
                        if debug == 1:Logging.LogInput.Log(
                            id,
                            round,
                            "Normal Payout: {} "
                            "Player Score: {} "
                            "Dealer Score: {} "
                            "old purse: {} "
                            "New Purse: {} "
                            "Current Bet Amount: {}"
                            .format(
                                p._cbet,
                                h._score,
                                settings.dealersScore,
                                op,
                                p._purse,
                                p._cbet
                                )
                            )
                elif (h._result == "Lose"):
                    p._lastroundpayout = p._cbet
                    p._purse -= p._lastroundpayout
                    if debug == 1:Logging.LogInput.Log(
                        id,
                        round,
                        "You Lose: {} "
                        "Player Score: {} "
                        "Dealer Score: {} "
                        "old purse: {} "
                        "New Purse: {} "
                        "Current Bet Amount: {}"
                        .format(
                            p._cbet,
                            h._score,
                            settings.dealersScore,
                            op,
                            p._purse,
                            p._cbet
                            )
                        )
                elif (h._result == 'Push'):
                    if debug == 1:Logging.LogInput.Log(
                        id,
                        round,
                        "Push: {}"
                        "Player Score: {} "
                        "Dealer Score: {} "
                        "old purse: {} "
                        "New Purse: {} "
                        "Current Bet Amount: {}"
                        .format(
                            p._cbet*blackjackpayout,
                            h._score,
                            settings.dealersScore,
                            op,
                            p._purse,
                            p._cbet
                            )
                        )
                else:
                    if debug == 1:Logging.LogInput.Log(
                        id,
                        round,
                        "ERROR End of CalculatePayouts: {}"
                        "Player Score: {} "
                        "Dealer Score: {} "
                        "old purse: {} "
                        "New Purse: {} "
                        "Current Bet Amount: {}"
                        .format(
                            p._cbet*blackjackpayout,
                            h._score,
                            settings.dealersScore,
                            op,
                            p._purse,
                            p._cbet
                            )
                        )
        if (p._peakpurse < p._purse):
            p._peakpurse = p._purse
        from Counting.CountingHelpers import RoundCount
        roundCount = RoundCount(settings.players)
        settings.shoe._roundcount = roundCount
        currentCount = settings.shoe._totalcount
        CardsLeftInShoe = len(settings.shoe._cards)
        newCount = (currentCount+roundCount)/CardsLeftInShoe
        if (newCount < .1):
            if ((p._peakpurse*WalkAwayWin >= p._purse 
                    and p._peakpurse > WalkAwayWinLimit)
                or (p._peakpurse*WalkAwayWinBig >= p._purse 
                    and p._peakpurse >WalkAwayWinBigLimit)
                or (p._purse <= WalkAwayLoss)):
                if debug == 1:Logging.LogInput.Log(
                    -99999,
                    round,
                    "Walking Away: {} "
                    "Player Score: {} "
                    "Dealer Score: {} "
                    "old purse: {} "
                    "New Purse: {} "
                    "Peak Purse: {} "
                    "Current Bet Amount: {}"
                    .format(
                        p._cbet*blackjackpayout,
                        h._score,
                        settings.dealersScore,
                        op,
                        p._purse,
                        p._peakpurse,
                        p._cbet
                        )
                    )
                settings.WalkAway = 1
                print(
                    "Walking Away",
                      settings.players[0]._purse,
                      settings.round, 
                      float("{0:.2f}".format(settings.shoe._percentagecount)),
                      float("{0:.2f}".format(settings.shoe._percentagecountpreviousround))
                    )
            else: 
                continue
        else: 
            continue
    return

