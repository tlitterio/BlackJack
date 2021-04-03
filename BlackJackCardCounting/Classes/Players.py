class Player(object):
    _index = int
    _label = str
    _active = int
    _purse = int
    _lastroundpayout = int
    _ibet = int
    _cbet = int
    _result = int
    _hands = []
    
    def __init__(player,label,index,active):
        player._index = index
        player._label = label
        player._active = active
        player._purse = 0
        player._peakpurse = 0
        player._lastroundpayout = 0
        player._ibet = 0
        player._cbet = 0
        player._hands = []
        player._result = "N/A"
