class Simulation(object):
    def __init__(self,
            Counting = None,
            ReshufflePercentage = None,
            ReshuffleMean = None,
            NumberOfPlayers = None,
            MinBet = None,
            MaxBet = None,
            WalkAwayLoss = None,
            WalkAwayWin = None,
            WalkAwayWinLimit = None,
            WalkAwayWinBig = None,
            WalkAwayWinBigLimit = None,
            definition = None,
            ):
    #region objects
        self.Counting = Counting
        self.ReshufflePercentage = ReshufflePercentage
        self.ReshuffleMean = ReshuffleMean
        self.NumberOfPlayers = NumberOfPlayers
        self.MinBet = MinBet
        self.MaxBet = MaxBet
        self.WalkAwayLoss = WalkAwayLoss
        self.WalkAwayWin = WalkAwayWin
        self.WalkAwayWinLimit = WalkAwayWinLimit
        self.WalkAwayWinBig = WalkAwayWinBig
        self.WalkAwayWinBigLimit = WalkAwayWinLimit
        self.definition = definition
        #endregion
