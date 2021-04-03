class Hand(object):
    _id = int
    _cards = []
    _hand = []
    _player = int
    _iteration = int
    _results = str
    _results = []
    _test = str
    _duplicate = int
    _score = int
    _cardsinhand = int
    _split = int
    _sibling = int
    _algo = int
    _bigaces = int
    _littleaces = int
    _closed = int
    def __init__(hand):
        hand._cards = []
        hand._hand = []
        hand._dealer = 0
        hand._iteration = 0
        hand._result = ""
        hand._results = []
        hand._test = ""
        hand._duplicate = 0
        hand._score = 0
        hand._cardsinhand = 0
        hand._dealersvisiblecardvalue = 0
        hand._split = 0
        hand._sibling = 0
        hand._algo = 0
        hand._bigaces = 0
        hand._littleaces = 0
        hand._closed = 0

