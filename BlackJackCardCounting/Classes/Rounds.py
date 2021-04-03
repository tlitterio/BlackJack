class Round(object):
    def __init__(self,
    #region objects
                Id,
                Counting,
                Set,
                Round,
                Iteration,
                Shoe,
                Discarded,
                Player,
                Purse,
                Hand,
                Algo,
                Card,
                DealersVisibleCardValue,
                Split,
                Sibling,
                Score,
                CardFace,
                ResultArray,
                CardSuit,
                CardValue,
                CardIndex,
                Result,
                TotalCount,
                RoundCount,
                ShoePercent,
                ShoePercentPreviousRound,
                InitBet,
                CurrentBet,
                Payout
            ):
        #endregion
        self.Id = Id
        self.Counting = Counting
        self.Set = Set
        self.Round = Round
        self.Iteration = Iteration
        self.Shoe = Shoe
        self.Discarded = Discarded
        self.Player = Player
        self.Purse = Purse
        self.Hand = Hand
        self.Algo = Algo
        self.Card = Card
        self.DealersVisibleCardValue = DealersVisibleCardValue
        self.Split = Split
        self.Sibling = Sibling
        self.Score = Score
        self.CardFace = CardFace
        self.ResultArray = ResultArray
        self.CardSuit = CardSuit
        self.CardValue = CardValue
        self.CardIndex = CardIndex
        self.Result = Result
        self.TotalCount = TotalCount
        self.RoundCount = RoundCount
        self.ShoePercent = ShoePercent
        self.ShoePercentPreviousRound = ShoePercentPreviousRound
        self.InitBet = InitBet
        self.CurrentBet = CurrentBet
        self.Payout = Payout

    def __iter__(self):
        yield 'Counting', self.Counting
        yield 'Set', self.Set
        yield 'Round', self.Round
        yield 'Iteration', self.Iteration
        yield 'Shoe', self.Shoe
        yield 'Discarded', self.Discarded
        yield 'Player', self.Player
        yield 'Purse', self.Purse
        yield 'Hand', self.Hand
        yield 'Algo', self.Algo
        yield 'Card', self.Card
        yield 'Split', self.Split
        yield 'Sibling', self.Sibling
        yield 'Score', self.Score
        yield 'CardFace', self.CardFace
        yield 'ResultArray', self.ResultArray
        yield 'CardSuit', self.CardSuit
        yield 'CardValue', self.CardValue
        yield 'CardIndex', self.CardIndex
        yield 'Result', self.Result
        yield 'TotalCount', self.TotalCount
        yield 'RoundCount', self.RoundCount
        yield 'ShoePercent', self.ShoePercent
        yield 'ShoePercentPreviousRound', self.ShoePercentPreviousRound
        yield 'InitBet', self.InitBet
        yield 'CurrentBet', self.CurrentBet
        yield 'Payout', self.Payout
