#import if debug == 1:Logging.LogInput
#import TableHelpers
#import Classes.Hands

#def OpenHands(player):
#    count =0
#    for h in player._hand:
#        if h._closed == 0:
#            count +=1
#    return count
#def ResetAceValue(hand):
#    for c in hand._cards:
#        if c._cardFace == "Ace":
#            c._value = 11
#    return hand
#def DoubleDown(hand):
#    hand = AddCard(hand)
#    hand = ScoreKeeper(hand)
#    hand._closed = 1
#    return hand
