#import _gv
#import Deal
#import Cards
#import Standard

#region Garbage
#def StandardMethod(hand,dealer):
#    dealerVisibleCard = dealer._hand[0]._cards[1]
#    dealerVisibleCardVal = dealerVisibleCard._value
#    playersCardLength = len(hand._cards)
#    if (hand._dealer == 1):
#        TempAction = DealerLogic(hand)
#        return TempAction
#    elif (hand._dealer == 0):
#        TempAction = ""
#        while TempAction == "":
#            TempAction = Algorithm(hand,dealerVisibleCardVal)
#            if (TempAction != ""):
#                return TempAction
#            else:
#                hand._algo = -1
#                TempAction = "ERROR"
#                return TempAction
#    else: 
#        TempAction = "BigERROR"
#        return TempAction


#def Algorithm(hand,dealerVisibleCardVal):
#    #hand = Deal.ScoreKeeper(hand)
#    BigAces = hand._bigaces
#    LittleAces = hand._littleaces
#    AcesCount = BigAces+LittleAces
#    playersCardLength = len(hand._cards)
#    otherCard = OtherCard(hand)
#    if playersCardLength == 2:
#        if (hand._score == 21):
#            TempAction = "BlackJack"
#            hand._algo = 1
#            return TempAction
#        elif (AcesCount == 1 and otherCard in range(8,10+1)):
#            TempAction = "Stand"
#            return TempAction
#        elif (AcesCount == 2):
#            TempAction = "Split"
#            return TempAction
#        elif (hand._cards[0]._value == 10 and hand._cards[1]._value == 10):
#            TempAction = "Stand"
#            return TempAction
#        elif (hand._score >=17 and BigAces == 0):
#            TempAction = "Stand"
#            return TempAction
#        elif hand._cards[0]._value == hand._cards[1]._value:
#            TempAction = DupAlgorithm(hand,dealerVisibleCardVal)
#            if TempAction != "":
#                hand._algo = 3
#                return TempAction
#        elif AcesCount in range(1,2+1):
#            TempAction = AceAlgorithm(hand,dealerVisibleCardVal)
#            if TempAction != "":
#                hand._algo = 2
#                return TempAction
#        else:
#            TempAction = RegularLogic(hand,dealerVisibleCardVal)
#            if TempAction != "":
#                hand._algo = 4
#                return TempAction
#    else:
#        if (hand._score == 21):
#            TempAction = "BlackJack;" # >2 Cards; >=22"
#            return TempAction
#        elif (hand._score > 21 and hand._bigaces == 0):
#            TempAction = "Busted;" # >2 Cards; >=22"
#            return TempAction
#        elif (hand._score >= 17 and hand._bigaces == 0):
#            TempAction = "Stand;"# >2 Cards; Hard 17"
#            return TempAction
#        elif (hand._score >= 19 and hand._bigaces == 1):
#            TempAction = "Stand" # >2 Cards; Soft 19"
#            return TempAction
#        elif (hand._score == 18 and hand._bigaces != 0):
#            if (dealerVisibleCardVal in range(9,11+1)):
#                TempAction = "Hit;"
#                return TempAction
#            else:
#                TempAction = "Stand;"
#                return TempAction

#        TempAction = RegularLogic(hand,dealerVisibleCardVal)
#        if TempAction != "":
#            hand._algo = 10
#            return TempAction
#        else:
#            TempAction = "ERROR;"
#            return TempAction
#def AceAlgorithm(hand,dealerVisibleCardVal):
#    hand._algo = 463
#    BigAces = hand._bigaces
#    LittleAces = hand._littleaces
#    AcesCount = BigAces+LittleAces
#    TempAction = ""
#    otherCard = OtherCard(hand)
#    if AcesCount == 2:
#        TempAction = "Split"
#        hand = ResetAceValue(hand)
#        return TempAction
#    elif (otherCard in range(2,3+1)):
#        if dealerVisibleCardVal in range(5,6+1):
#            TempAction = "Double"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (otherCard in range(4,5+1)):
#        if dealerVisibleCardVal in range(4,6+1):
#            TempAction = "Double"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (otherCard == 6):
#        if dealerVisibleCardVal in range(3,6+1):
#            TempAction = "Double"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (otherCard == 7):
#        if (dealerVisibleCardVal == 2 
#            or dealerVisibleCardVal in range(7,8+1)):
#            TempAction = "Stand"
#            return TempAction
#        elif (dealerVisibleCardVal in range(3,6+1)):
#            TempAction = "Double/Stand"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (otherCard in range(8,10+1)):
#        TempAction = "Stand"
#        return TempAction
#    else:
#        TempAction = ""
#        return TempAction
#def DupAlgorithm(hand,dealerVisibleCardVal):
#    hand._algo = 22
#    TempAction = ""
#    handscore = hand._score
#    duplicate = hand._cards[0]._value
#    if (duplicate == 3):
#        test = 0
#    if (duplicate == 2):
#        if dealerVisibleCardVal in range(2,7+1):
#            TempAction = "Split"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (duplicate == 3):
#        if dealerVisibleCardVal in range(2,7+1):
#            TempAction = "Split"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (duplicate == 4):
#        if dealerVisibleCardVal in range(5,6+1):
#            TempAction = "Split"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (duplicate == 5):
#        TempAction = RegularLogic(hand,dealerVisibleCardVal)
#        return TempAction
#    elif (duplicate == 6):
#        if dealerVisibleCardVal in range(2,6+1):
#            TempAction = "Split"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (duplicate == 7):
#        if dealerVisibleCardVal in range(2,7+1):
#            TempAction = "Split"
#            return TempAction
#        else:
#            TempAction = "Hit"
#            return TempAction
#    elif (duplicate == 8):
#        TempAction = "Split"
#        return TempAction
#    elif (duplicate == 9):
#        if (dealerVisibleCardVal == 7 
#            or dealerVisibleCardVal in range(10,11+1)):
#            TempAction = "Stand"
#            return TempAction
#        else:
#            TempAction = "Split"
#            return TempAction
#    elif (duplicate == 10):
#        TempAction = "Stand"
#        return TempAction
#    else:
#        TempAction = ""
#        return TempAction

#def RegularLogic(hand,dealerVisibleCardVal):
#    #hand = Deal.HandleAces(hand)
#    if hand._iteration == 0: hand._algo = 936
#    TempAction = ""
#    if (len(hand._cards) > 2 and hand._score ==18 and hand._bigaces == 1):
#        TempAction = "Stand"
#        return TempAction

#    if (hand._score > 21 and hand._soft > 1):
#        hand = Deal.ScoreKeeper(hand)
#    if ((hand._score in range(17,21+1) and hand._bigaces == 0) 
#        or (hand._score in range(19,21+1) and hand._bigaces == 1)):
#        TempAction = "Stand"
#        return TempAction
#    #if ((hand._score == 17 and hand._bigaces == 0)): 
#    #    TempAction = "Stand"
#    #    return TempAction
#    if ((hand._score == 4 and hand._soft == 1)): 
#        TempAction = "WTF-4;"
#        return TempAction
#    if (hand._score > 21 and hand._soft == 0):
#        TempAction = "Busted"
#        return TempAction

#    if (hand._score in range(5,8+1)): 
#        TempAction = "Hit"
#        return TempAction
#    elif (hand._score == 9):
#        if (dealerVisibleCardVal in range(3,6+1)):
#            TempAction = "Double/Hit"
#            return TempAction
#        else: 
#            TempAction = "Hit"
#            return TempAction
#    elif (hand._score == 10):
#        if (dealerVisibleCardVal in range(2,9+1)):
#            TempAction = "Double/Hit"
#            return TempAction
#        else: 
#            TempAction = "Hit"
#            return TempAction
#    elif (hand._score == 11):
#        if (dealerVisibleCardVal in range(2,10+1)):
#            TempAction = "Double/Hit"
#            return TempAction
#        else: 
#            TempAction = "Hit"
#            return TempAction
#    elif (hand._score == 12):
#        if (dealerVisibleCardVal in range(4,6+1)):
#            TempAction = "Stand"
#            return TempAction
#        else: 
#            TempAction = "Hit"
#            return TempAction
#    elif (hand._score == 13):
#        if (dealerVisibleCardVal in range(2,6+1)):
#            TempAction = "Stand"
#            return TempAction
#        else: 
#            TempAction = "Hit"
#            return TempAction
#    elif (hand._score == 14):
#        if (dealerVisibleCardVal in range(2,6+1)):
#            TempAction = "Stand"
#            return TempAction
#        else: 
#            TempAction = "Hit"
#            return TempAction
#    elif (hand._score == 15):
#        if (dealerVisibleCardVal in range(2,6+1)):
#            TempAction = "Stand"
#            return TempAction
#        elif (dealerVisibleCardVal == 10):
#            TempAction = "Surrender/Hit"
#            return TempAction
#        else: 
#            TempAction = "Hit"
#            return TempAction
#    elif (hand._score == 16):
#        if (dealerVisibleCardVal in range(2,6+1)):
#            TempAction = "Stand"
#            return TempAction
#        elif (dealerVisibleCardVal in range(9,11+1)):
#            TempAction = "Surrender/Hit"
#            return TempAction
#        else: 
#            TempAction = "Hit"
#            return TempAction
#    elif (hand._score ==17 and hand._bigaces != 0):
#        TempAction = "Hit;"
#        return TempAction
#    #elif (hand._score ==17):
#    #    TempAction = "18-ERROR; Regular Logic - Last elif"
#    #    return TempAction
#    else: 
#        TempAction = "ERROR; Catch All Regular Logic"
#        return TempAction
#def DealerLogic(hand):
#    hand._algo = 3479
#    hand = Deal.ScoreKeeper(hand)
#    TempAction = ""
#    if (hand._score > 21 and hand._soft == 1):
#        hand = Deal.ScoreKeeper(hand)
#    if (hand._score > 21 and hand._soft == 0):
#        TempAction = "Busted"
#        return TempAction
#    if (hand._score >= 17): 
#        TempAction = "Stand"
#        return TempAction
#    else: 
#        TempAction = "Hit"
#        return TempAction
#def OtherCard(hand):
#    Count = 0
#    for c in hand._cards:
#        if c._cardFace != "Ace":
#            return c._value
#    return Count


#def AcesCount(hand):
#    Count = 0
#    for c in hand._cards:
#        if c._cardFace == "Ace":
#            Count += 1
#    return Count
#def BigAcesCount(hand):
#    Count = 0
#    for c in hand._cards:
#        if c._cardFace == "Ace" and c._value == 11:
#            Count += 1
#    return Count
#def LittleAcesCount(hand):
#    Count = 0
#    for c in hand._cards:
#        if c._cardFace == "Ace" and c._value == 1:
#            Count += 1
#    return Count





#global SplitAlgoMatrix; SplitAlgoMatrix = [
#    28,
#    30,
#    31,
#    34,
#    35,
#    36,
#    37,
#    47,
#    49,
#    50,
#    53,
#    54,
#    55,
#    56,
#    84,
#    86,
#    87,
#    90,
#    91,
#    92,
#    93,
#    145,
#    147,
#    148,
#    149,
#    151,
#    152,
#    153,
#    154,
#    236,
#    238,
#    239,
#    240,
#    242,
#    243,
#    244,
#    245,
#    363,
#    365,
#    366,
#    370,
#    371,
#    532,
#    540,
#    541,
#    749,
#    757,
#    758,
#    1020,
#    1028,
#    1351,
#    1359]
#global HitAlgoMatrix; HitAlgoMatrix = [
#    20,
#    21,
#    22,
#    23,
#    24,
#    32,
#    39,
#    40,
#    41,
#    42,
#    51,
#    76,
#    77,
#    88,
#    355,
#    356,
#    357,
#    358,
#    359,
#    367,
#    369,
#    524,
#    525,
#    526,
#    527,
#    528,
#    534,
#    535,
#    536,
#    538,
#    539,
#    741,
#    742,
#    743,
#    744,
#    745,
#    746,
#    751,
#    752,
#    753,
#    755,
#    756,
#    1012,
#    1013,
#    1014,
#    1015,
#    1016,
#    1017,
#    1022,
#    1023,
#    1024,
#    1026,
#    1027,
#    1343,
#    1344,
#    1345,
#    1346,
#    1347,
#    1348,
#    1353,
#    1354,
#    1355,
#    1357,
#    1358]
#global DoubleAlgoMatrix; DoubleAlgoMatrix = [
#    43,
#    78,
#    79,
#    80,
#    137,
#    138,
#    139,
#    140,
#    141,
#    228,
#    229,
#    230,
#    231,
#    232]
#global DoubleStandAlgoMatrix; DoubleStandAlgoMatrix = [
#    44,
#    81,
#    142,
#    233]
#global StandAlgoMatrix; StandAlgoMatrix = [
#    25,
#    360,
#    372,
#    529,
#    1029,
#    1360]

    #TempAction = ""
    #DealersCard = Deal.DealersVisibleCard()
    #algoScore = 0
    #Aces = 0
    #CardVal = 0
    #for c in hand._cards:
    #    if c._cardFace == "Ace": 
    #        algoScore+=10
    #        Aces +=1
    #    elif c._value == 10: 
    #        algoScore += 0
    #    else: 
    #        CardVal = c._value
    #        algoScore += c._value
    
    #if (algoScore < 20 
    #    and hand._cards[0]._value == hand._cards[1]._value 
    #    and hand._cards[0]._value != 10 
    #    and hand._cards[0]._value != 5): 
    #    algo = ((algoScore / 2) + 20)+(DealersCard._value)**3

    #elif (Aces==1):
    #    algoScore = 20+CardVal
    #    algo = algoScore+((DealersCard._value)**3)
    #else: algo = algoScore
    #if algo in SplitAlgoMatrix: TempAction = "Split"
    #elif algo in HitAlgoMatrix: TempAction = "Hit"
    #elif algo in DoubleAlgoMatrix: TempAction = "Double"
    #elif algo in DoubleStandAlgoMatrix: TempAction = "Double"
    #elif algo in StandAlgoMatrix: TempAction = "Stand"
    #return TempAction

    #elif (playersHand._score >=17) and ("Ace" not in playersHand 
    #    and ("King" not in playersHand 
    #        or "Queen" not in playersHand 
    #        or "Jack" not in playersHand 
    #        or "Ten" not in playersHand 
    #        or "Nine" not in playersHand 
    #        or "Eight" not in playersHand)): 
    #    player._result = "Stand"
    #elif (playersHand.

#    else: return
#    #region Player Logic
#    if (player._index != dealer._index): 
#        if (PlayersScore == 21): 
#            player._result = "BlackJack!" 
#        elif ((len(playersHand) == 2) 
#              and (playersHand[0]._value == playersHand[1]._value) 
#              and ((playersHand[0]._value == range(2,4)) 
#                   or (playersHand[0]._value == range(6,9)))): 
#            player._result = "Split"
#            #playersHand[0].pop()



#        if (hand._score == 9 
#            and dealerVisibleCard._value in range(3,6+1)): 
#            return _TempAction
#        elif (hand._score == 10 
#            and dealerVisibleCard._value in range(2,9+1)): 
#            return _TempAction
#        elif (hand._score == 11 
#            and dealerVisibleCard._value in range(2,10+1)): 
#            return _TempAction
#        else:
#            _TempAction = "Stand"
#            if (hand._score == 12 
#                and (dealerVisibleCard._value in range(4,6+1))): 
#                return _TempAction
#            elif (hand._score in range(13,16+1) 
#                and (dealerVisibleCard._value in range(2,6+1))): 
#                return _TempAction
#            elif (hand._score in range(13,16+1) 
#                and (dealerVisibleCard._value in range(2,6+1))): 
#                return _TempAction
#            else:
#                _TempAction = "Surrender/Hit"
#                if (hand._score == 15 
#                    and (dealerVisibleCard._value == 10)): 
#                    return _TempAction
#                elif (hand._score == 16 
#                    and (dealerVisibleCard._value in range(9,11+1))): 
#                    return _TempAction
#                else: 
#                    _TempAction = "Hit"
#                    return _TempAction



#        elif (playersHand == range(3,8)): 
#            player._result =  "Hit"
#        elif (len(playersHand) ==2):
#            #if (PlayersHand):
#            player._result = "STuff"
#        else: player._result = "Cought"
#    #endregion

#    #region Dealer Logic
#    elif (player._index != dealer._index): 
#        dealer._result = "Dealer"
#    #endregion
#    else: print("ERROR")
#def GetScore(player):
#    tempHands = len(player._hand)
#Constants
#Never Take insurance
#Always Stand hard 17 or higher
#Always stand A8, A9, A10 and 10-10
#Always play 5-5 as 10
#Always split Aces

#HITs
#Player showing 5-8 with dealer showing any value
#Player showing 9 with dealer showing 2 or 7-A
#Player showing 10 with dealer showing 10 or A
#Player showing 11 with dealer showing A
#Player showing 12 with dealer showing 2,3 or 7-A
#Player showing 13 with dealer showing 7-A
#Player showing 14 with dealer showing 7-A
#Player showing 15 with dealer showing 7-9 or A
#Player showing 16 with dealer showing 7-8
#Player showing A2 with dealer showing 2-4 or 7-A
#Player showing A3 with dealer showing 2-4 or 7-A
#Player showing A4 with dealer showing 2-3 or 7-A
#Player showing A5 with dealer showing 2-3 or 7-A
#Player showing A6 with dealer showing 2 or 7-A
#Player showing A7 with dealer showing 9-A
#Player showing 2-2 with dealer showing 8-A
#Player showing 3-3 with dealer showing 8-A
#Player showing 4-4 with dealer showing 2-4 or 7-A
#Player showing 6-6 with dealer showing 7-A
#Player showing 7-7 with dealer showing 8-A


#Player showing 5-8 with dealer showing any value should Hit
#Player showing 5-8 with dealer showing any value should Hit


#    #region bottom quarter of Basic Strategy Card (What to do when cards equal each other)
#        playerFirstCard = hand._cards[0]
#        playerSecondCard = hand._cards[1]
#        if (playerFirstCard._cardFace==playerSecondCard._cardFace):
#            _TempAction = "Split"
#            if (playerFirstCard == "Ace" 
#                or playerFirstCard == "Eight"): 
#                return _TempAction
#            elif (playerFirstCard == "Nine" 
#                  and (dealerVisibleCard._value != 7 
#                       or dealerVisibleCard._value != range(10,11+1))):
#                  return _TempAction
#            elif (playerFirstCard == "Two"
#                    and dealerVisibleCard._value != range(8,11+1)):
#                    return _TempAction
#            elif (playerFirstCard == "Three"
#                    and dealerVisibleCard._value != range(8,11+1)): 
#                    return _TempAction
#            elif (playerFirstCard == "Four"
#                    and (dealerVisibleCard._value != range(2,4+1) 
#                    or dealerVisibleCard._value != range(7,11+1))): 
#                    return _TempAction
#            elif (playerFirstCard == "Six" 
#                    and dealerVisibleCard._value != range(7,11+1)): 
#                    return _TempAction
#            elif (playerFirstCard == "Seven" 
#                    and dealerVisibleCard._value != range(8,11+1)): 
#                    return _TempAction
#            elif (playerFirstCard != "Nine"):
#                _TempAction = "Hit"
#                return _TempAction
#            else:  
#                _TempAction="Stand"
#                return _TempAction

#    #region 3rd Quarter; player is showing 1 Ace
#        elif (AcesCount == 1):
#            _TempAction = "Double/Hit"
#            if (hand._score >= 19):
#                _TempAction = "Stand"
#                return _TempAction
#            elif ((playerFirstCard._cardFace in range(2,3+1) 
#                    or playerSecondCard._cardFace == range(2,3+1)) 
#                and (dealerVisibleCard._value in range(5,6+1))):
#                return _TempAction
#            elif ((playerFirstCard._cardFace in range(4,5+1) 
#                    or playerSecondCard._cardFace == range(4,5+1)) 
#                and (dealerVisibleCard._value in range(4,6+1))):
#                return _TempAction
#            elif ((playerFirstCard._cardFace in range(6,7+1) 
#                    or playerSecondCard._cardFace == range(6,7+1)) 
#                and (dealerVisibleCard._value in range(3,6+1))):
#                return _TempAction
#            elif ((playerFirstCard._cardFace in range(6,7+1) 
#                    or playerSecondCard._cardFace == range(6,7+1)) 
#                and (dealerVisibleCard._value == 2 
#                or dealerVisibleCard._value == range(3,6+1))):
#                return _TempAction
#            elif dealerVisibleCard._value in range(7,8+1):
#                return _TempAction
#        else: 
#            _TempAction = RegularLogic(hand)
#            return _TempAction
#endregion



