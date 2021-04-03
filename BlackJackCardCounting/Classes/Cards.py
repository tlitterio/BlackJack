class Card(object):
    _index = int
    _roundId = int
    _mainId = int
    _deck = int
    _value = int
    _cardFace = str
    _suit = int
    _suitFace = str
    def __init__(card,index,deck,value,cardFace,suit,suitFace):
        card._index = index
        card._deck = deck
        card._value = value
        card._cardFace = cardFace
        card._suit = suit
        card._suitFace = suitFace

#region Logic Testing
    def Ace11():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 11,
            dealerx = 0,
            cardFace = "Ace11",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Ace1():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 1,
            dealerx = 0,
            cardFace = "Ace1",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Face():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 10,
            dealerx = 0,
            cardFace = "Face",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Ten():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 10,
            dealerx = 0,
            cardFace = "Ten",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Nine():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 9,
            dealerx = 0,
            cardFace = "Nine",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Eight():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 8,
            dealerx = 0,
            cardFace = "Eight",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Seven():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 7,
            dealerx = 0,
            cardFace = "Seven",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Six():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 6,
            dealerx = 0,
            cardFace = "Six",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Five():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 5,
            dealerx = 0,
            cardFace = "Five",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Four():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 4,
            dealerx = 0,
            cardFace = "Four",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Three():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 3,
            dealerx = 0,
            cardFace = "Three",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

    def Two():
        tCard = Card(
            index = -1,
            deck = -1,
            value = 2,
            dealerx = 0,
            cardFace = "Two",
            suit = -1,
            suitFace = "N/A"
        )
        return tCard

#endregion
