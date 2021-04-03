import settings
import Logging.LogInput
from settings import debug

def StandardMethod(hand):
    id = 500

    round = settings.round
    if (hand._results != []):
        LastActionResult = hand._results[len(hand._results)-1]
        if debug == 1:Logging.LogInput.Log(id,
                             round,
                             "     Last Action Result Was: {}"
                             .format(LastActionResult))
    cardsInHand = len(hand._cards)
    dvcv = settings.dealersvisiblecardvalue
    score = hand._score
    soft = hand._bigaces
    duplicate = hand._duplicate
    aces = hand._bigaces+hand._littleaces
    bigAces = hand._bigaces
    result = ""
    #handStr = ''.join(str(e) for e in hand._hand)
    handStr =""
    for i in hand._hand:
        handStr += str(i)
        handStr += ","
    
    if debug == 1:Logging.LogInput.Log(id,
                         round,
                         "Starting Standard Method Method: {}:{} - {}"
                         .format(handStr,hand._score,dvcv))

    testing = 0
    if testing == 1:
        hand._hand = [11,11]
        hand._score = 22
        aces = 2
        bigAces = 1
        dvcv = 2
        hand._duplicate = 11
        hand._dealer = 0
    #region Dealer Handling    
    if (settings.dealersScore == 21 and cardsInHand == 2):
        id = 501
        if debug == 1:Logging.LogInput.Log(id,
                             settings.round,
                             "Dealer BlackJack, Round Over: {}:{} - {}"
                             .format(handStr,hand._score,dvcv))
        hand._results.append("DealerBlackJack")
        return hand #DealerBlackJack
    elif (hand._dealer == 1): #Dealer Logic
        id = 502
        if debug == 1:Logging.LogInput.Log(id,
                             settings.round,
                             "Executing Dealer Logic: {}:{} - {}"
                             .format(handStr,hand._score,dvcv))
        result = DealerLogic(hand)
        hand._results.append(result)
        if debug == 1:Logging.LogInput.Log(id,settings.round,result)
        return hand
    #endregion
    
    elif (hand._score == 21 and cardsInHand == 2 and hand._split == 0):
        id = 510
        if debug == 1:Logging.LogInput.Log(id,
                             settings.round,
                             "Player BlackJack: {}:{} - {}"
                             .format(handStr,hand._score,dvcv))
        hand._results.append("BlackJack")
        return hand #BlackJack
    elif (cardsInHand == 2 and hand._duplicate != 0): # and hand._split == 0):
        id = 511
        if debug == 1:Logging.LogInput.Log(id,
                             settings.round,
                             "Executing Duplicate Test: {}:{} - {}"
                             .format(handStr,hand._score,dvcv))
        duplicate = hand._duplicate
        hand._duplicate = 0
        result = DuplicateActions(duplicate,dvcv)
        if debug == 1:Logging.LogInput.Log(id,
                                           settings.round,
                                           result)
        hand._results.append(result)
        return hand #Run Through duplicate logic
    elif (soft > 0):
        id = 512
        if debug == 1:Logging.LogInput.Log(id,
                             settings.round,
                             "Executing Soft Test: {}:{} - {}"
                             .format(handStr,hand._score,dvcv))
        result = SoftActions(hand,dvcv)
        if debug == 1:Logging.LogInput.Log(id,settings.round,result)
        hand._results.append(result)
        return hand
    elif (soft == 0):
        id = 513
        if debug == 1:Logging.LogInput.Log(id,
                             settings.round,
                             "Executing Hard Test: {}:{} - {}"
                             .format(handStr,hand._score,dvcv))
        result = HardActions(hand,dvcv)
        if debug == 1:Logging.LogInput.Log(id,
                                           settings.round,
                                           result)
        hand._results.append(result)
        return hand
    else:
        id = 550
        hand._results.append("ERROR - End of StandardMethod; {}:{} - {}"
                             .format(handStr,
                                     hand._score,
                                     dvcv))
        hand._closed = 1
        return hand

def DuplicateActions(duplicate,dvcv):
    try:
        test = [duplicate,dvcv]
        #region DuplicateActions Arrays
        DuplicateSplitArray = [
            [2,2],
            [2,3],
            [2,4],
            [2,5],
            [2,6],
            [2,7],
            [3,2],
            [3,3],
            [3,4],
            [3,5],
            [3,6],
            [3,7],
            [4,5],
            [4,6],
            [6,2],
            [6,3],
            [6,4],
            [6,5],
            [6,6],
            [7,2],
            [7,3],
            [7,4],
            [7,5],
            [7,6],
            [7,7],
            [9,2],
            [9,3],
            [9,4],
            [9,5],
            [9,6],
            [9,8],
            [9,9],
            ]
        DuplicateHitArray = [
            [4,2],
            [4,3],
            [4,4],
            [2,8],
            [2,9],
            [2,10],
            [2,11],
            [3,8],
            [3,9],
            [3,10],
            [3,11],
            [4,7],
            [4,8],
            [4,9],
            [4,10],
            [4,11],
            [6,7],
            [6,8],
            [6,9],
            [6,10],
            [6,11],
            [7,8],
            [7,9],
            [7,10],
            [7,11],
        ]
        DuplicateStandArray = [
            [9,7],
            [9,10],
            [9,11],   
        ]
        HardStand = [10]
        HardSplit = [8,11]
        #endregion

        if (duplicate == 5):
            if (dvcv in range(2,9+1)):
                return "FiveDouble - DuplicateActions"
            else: 
                return "FiveHit - DuplicateActions"
        elif (duplicate in HardSplit):
             return "HardSplit - DuplicateActions"
        elif (duplicate in HardStand):
            return "HardStand - DuplicateActions"
        elif (test in DuplicateSplitArray):
             return "DuplicateSplitArray - DuplicateActions"
        elif (test in DuplicateHitArray):
            return "DuplicateHitArray - DuplicateActions"
        elif (test in DuplicateStandArray):
            return "DuplicateStandArray - DuplicateActions"
        else: 
            return "ERROR - End of DuplicateActions;else"
    except:
        e = sys.exc_info()[0]
        if debug == 1:Logging.LogInput.Log(id,
                                           settings.round,
                                           e)
def SoftActions(hand,dvcv):
    try:
        global othercard
        Score = hand._score
        Soft = hand._bigaces
        test = [Score,dvcv,Soft]
        if (Score in range(19,21+1)): 
            return "HardStand - SoftActions"
        othercard = OtherCard(hand)
        #region SoftActions Arrays
        HardDouble = [12]
        DoubleHitArray = [
                [13,5,1],
                [13,6,1],
                [14,5,1],
                [14,6,1],
                [15,4,1],
                [15,5,1],
                [15,6,1],
                [16,4,1],
                [16,5,1],
                [16,6,1],
                [17,3,1],
                [17,4,1],
                [17,5,1],
                [17,6,1],
            ]
        DoubleStandArray = [
                [18,3,1],
                [18,4,1],
                [18,5,1],
                [18,6,1],
            ]
        StandArray = [
                [18,2,1],
                [18,7,1],
                [18,8,1],
            ]
        HitArray = [
                [13,2,1],
                [13,3,1],
                [13,4,1],
                [13,7,1],
                [13,8,1],
                [13,9,1],
                [13,10,1],
                [13,11,1],
                [14,2,1],
                [14,3,1],
                [14,4,1],
                [14,7,1],
                [14,8,1],
                [14,9,1],
                [14,10,1],
                [14,11,1],
                [15,2,1],
                [15,3,1],
                [15,7,1],
                [15,8,1],
                [15,9,1],
                [15,10,1],
                [15,11,1],
                [16,2,1],
                [16,3,1],
                [16,7,1],
                [16,8,1],
                [16,9,1],
                [16,10,1],
                [16,11,1],
                [17,2,1],
                [17,7,1],
                [17,8,1],
                [17,9,1],
                [17,10,1],
                [17,11,1],
                [18,9,1],
                [18,10,1],
                [18,11,1],

        ]
        #endregion
        if (Score == 21 and len(hand._cards) == 2):
             return "BlackJack - SoftActions"
        elif (Score in HardDouble and len(hand._cards) == 2 and hand._split > 0):
             return "HardDouble - SoftActions"
        elif (test in DoubleHitArray and len(hand._cards) == 2):
             return "Double - SoftActions"
        elif (test in DoubleHitArray and len(hand._cards) > 2):
             return "Hit - SoftActions"
        elif (test in DoubleStandArray and len(hand._cards) == 2):
            return "Double - SoftActions"
        elif (test in DoubleStandArray and len(hand._cards) > 2):
            return "Stand - SoftActions"
        elif (test in StandArray):
            return "Stand - SoftActions"
        elif (test in HitArray):
            return "Hit - SoftActions"
        else: 
            return "ERROR - End Of SoftActions;else"
    except:
        e = sys.exc_info()[0]
        if debug == 1:Logging.LogInput.Log(id,settings.round,e)
def HardActions(hand,dvcv):
    try:
        Score = hand._score
        Soft = hand._bigaces
        hardstests = [Score]
        test = [Score,dvcv,Soft]
        #region HardArray
        HardHits = [
            [4],
            [5],
            [6],
            [7],
            [8],
        ]
        HardStand = [
            [17],
            [18],
            [19],
            [20],
            [21],
        ]
        DoubleHits = [
            [9,3,0],
            [9,4,0],
            [9,5,0],
            [9,6,0],
            [10,2,0],
            [10,3,0],
            [10,4,0],
            [10,5,0],
            [10,6,0],
            [10,7,0],
            [10,8,0],
            [10,9,0],
            [11,2,0],
            [11,3,0],
            [11,4,0],
            [11,5,0],
            [11,6,0],
            [11,7,0],
            [11,8,0],
            [11,9,0],
            [11,10,0],
        ]
        Stand = [
            [12,4,0],
            [12,5,0],
            [12,6,0],
            [13,2,0],
            [13,3,0],
            [13,4,0],
            [13,5,0],
            [13,6,0],
            [14,2,0],
            [14,3,0],
            [14,4,0],
            [14,5,0],
            [14,6,0],
            [15,2,0],
            [15,3,0],
            [15,4,0],
            [15,5,0],
            [15,6,0],
            [16,2,0],
            [16,3,0],
            [16,4,0],
            [16,5,0],
            [16,6,0],
        ]
        Hit = [
            [9,2,0],
            [9,7,0],
            [9,8,0],
            [9,9,0],
            [9,10,0],
            [9,11,0],
            [10,10,0],
            [10,11,0],
            [11,11,0],
            [12,2,0],
            [12,3,0],
            [12,7,0],
            [12,8,0],
            [12,9,0],
            [12,10,0],
            [12,11,0],
            [13,7,0],
            [13,8,0],
            [13,9,0],
            [13,10,0],
            [13,11,0],
            [14,7,0],
            [14,8,0],
            [14,9,0],
            [14,10,0],
            [14,11,0],
            [15,7,0],
            [15,8,0],
            [15,9,0],
            [15,11,0],
            [16,7,0],
            [16,8,0],
        ]
        SurrenderHit = [
            [15,10,0],
            [16,9,0],
            [16,10,0],
            [16,11,0],
        ]
        #endregion
        if (Score > 21):
            return "Busted - HardActions"
        elif (hardstests in HardHits):
            return "HardHit - HardActions"
        elif (hardstests in HardStand):
            return "HardStand - HardActions"
        elif (test in DoubleHits and len(hand._cards) == 2):
            return "Double - HardActions"
        elif (test in DoubleHits and len(hand._cards) > 2):
            return "Hit - HardActions"
        elif (test in Stand):
            return "Stand - HardActions"
        elif (test in Hit):
            return "Hit - HardActions"
        elif (test in SurrenderHit):
            return "SurrenderHit - HardActions"
        else:
            return "ERROR - End of Hard Actions - END OF THE LINE"
    except:
        e = sys.exc_info()[0]
        if debug == 1:Logging.LogInput.Log(id,
                                           settings.round,
                                           e)
def DealerLogic(hand):
    try:
        if (hand._score in range(17,21+1)):
            return "Stand - DealerLogic"
        elif (hand._score > 21 and hand._bigaces == 0):
            return "Busted - DealerLogic"
        elif (hand._score < 17):
            return "Hit - DealerLogic"
        else:
            return "ERROR - DealerLogic"
    except:
        e = sys.exc_info()[0]
        if debug == 1:Logging.LogInput.Log(id,settings.round,e)
        if debug == 1:Logging.LogInput.Log(id,settings.round,"FU")
def OtherCard(hand):
    id = 75
    if debug == 1:Logging.LogInput.Log(id,settings.round,"Executing OtherCard Helper")
    try:
        Count = 0
        for c in hand._cards:
            if c._cardFace != "Ace":
                return c._value
        return Count
    except:
        e = sys.exc_info()[0]
        if debug == 1:Logging.LogInput.Log(id,settings.round,e)
