class Shoe(object):
    """description of class"""
    _cards = []
    _roundId = int
    _simulationId = int
    _totalcount = int
    _roundcount = int
    _percentagecount = float
    _percentagecountpreviousround = float
    _reshuffleRemaining = int
    def __init__(shoe):
        shoe._cards = []
        shoe._roundId = 0
        shoe._mainId = 0
        shoe._totalcount = 0
        shoe._roundcount = 0
        shoe._percentagecount = .00000
        shoe._percentagecountpreviousround = .00000
        shoe._reshuffleRemaining = 0
