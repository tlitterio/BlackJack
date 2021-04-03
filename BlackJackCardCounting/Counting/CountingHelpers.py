import TableHelpers
import Logging.LogInput
import settings
from settings import *

def GetCount():
    id = 100
    if debug == 1:Logging.LogInput.Log(id,settings.round,"Getting Counts")
    settings.shoe._percentagecountpreviousround = settings.shoe._percentagecount
    settings.shoe._totalcount = TotalCount(settings.shoe)
    settings.shoe._roundcount = RoundCount(settings.players)
    settings.shoe._percentagecount = RealCount(settings.shoe)

def RoundCount(players):
    id = 101
    count = 0
    if debug == 1:Logging.LogInput.Log(id,
                         TableHelpers.round,
                         "     Getting Round Count: {}"
                         .format(count))
    for p in players:
        for h in p._hands:
            for c in h._cards:
                if ((c._cardFace == "Ten")
                      or (c._cardFace == "Jack")
                      or (c._cardFace == "Queen")
                      or (c._cardFace == "King")
                      or (c._cardFace == "Ace")): count -= 1
                elif ((c._cardFace == "Six")
                      or (c._cardFace == "Five")
                      or (c._cardFace == "Four")
                      or (c._cardFace == "Three")
                      or (c._cardFace == "Two")): count += 1
                else: continue
    return count
def TotalCount(shoe):
    id = 102
    count = 0
    discarded = settings.discarded
    for c in discarded:
        if ((c._cardFace == "Ten")
              or (c._cardFace == "Jack")
              or (c._cardFace == "Queen")
              or (c._cardFace == "King")
              or (c._cardFace == "Ace")): count -= 1
        elif ((c._cardFace == "Six")
              or (c._cardFace == "Five")
              or (c._cardFace == "Four")
              or (c._cardFace == "Three")
              or (c._cardFace == "Two")): count += 1
        else: continue
    if debug == 1:Logging.LogInput.Log(id,
                         TableHelpers.round,
                         "     Getting Total Count: {}"
                         .format(count))
    return count
def RealCount(shoe):
    id = 110
    count = .000
    CardsLeftInShoe = len(shoe._cards)
    DecksLeftinShoe = CardsLeftInShoe/52
    CurrentCount = shoe._totalcount
    count = CurrentCount/CardsLeftInShoe
    if debug == 1:Logging.LogInput.Log(id,
                         TableHelpers.round,
                         "     Getting Count as Percentage of Cards Left in Shoe: {}"
                         .format(count))
    TableHelpers.realCount = count
    return count