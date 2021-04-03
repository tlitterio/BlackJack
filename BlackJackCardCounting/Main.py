import settings
settings.init()
from settings import *
from TableHelpers import *
import decimal
from Counting import CountingHelpers
from Logging import LogInput as Log
#Log.InitializeTables()
from Classes import Shoes
from Strategies.Analysis import PlayRound
from Counting.CountingHelpers import GetCount

#log.InitializeSimulation()

sim = 0
while sim == 0:
    sets = 1000000000
    setCounter = 1
    Log.RecordSimulationData()
    while setCounter <= sets:
        settings.shoe = Shoes.Shoe()
        settings.discarded = []
        settings.players = []
        settings.players = InitializePlayers()
        InitializeShoe()

        settings.WalkAway = 0
        while settings.WalkAway != 1:
            GetCount() #Do not move; previous round calculations are being done in the payout method
            ResetShoe()

            if debug == 1:
                Logging.LogInput.Log(3,
                        round,
                        "Starting Round: {}"
                        .format(settings.round))
                Logging.LogInput.Log(3,
                        round,
                        "Discarded Length: {}"
                        .format(len(settings.discarded)))
                Logging.LogInput.Log(3,
                        round,
                        "Shoe Length: {}"
                        .format(len(settings.shoe._cards)))
                Logging.LogInput.Log(3,
                        round,
                        "Total Count  (Pre Deal): {}"
                        .format(settings.shoe._totalcount))
                Logging.LogInput.Log(3,
                        round,
                        "Count Percentage of Shoe  (Pre Deal): {}"
                        .format(settings.shoe._percentagecount))
            
            DealHand()
            for p in settings.players:
                p = PlayRound(p,settings.round)
            ScoreRound()
            CalculatePayouts()
            #if debug == 1:Logging.LogInput.SerializeRecords()
            print(settings.players[0]._purse,
                  settings.players[0]._hands[0]._result,
                  settings.round, 
                  float("{0:.4f}"
                        .format(settings.shoe._percentagecount)),
                  float("{0:.4f}"
                        .format(settings.shoe._percentagecountpreviousround)))
            ##print(TableHelpers.round)
            #if round % RecordtoDbRound == 0:
            if settings.WalkAway == 1:
                test = 0
                #if debug == 1:Logging.LogInput.RecordSimulationData()
                #if debug == 1:Logging.LogInput.SerializeConfig()
                #if debug == 1:Logging.LogInput.PostRounds()
            ClearRound()
            settings.round+=1
        settings.set += 1
        setCounter +=1
    sim +=1
print("End")

        #round = settings.round
        #TableHelpers.Strategy = 3
        #while TableHelpers.Strategy <= 8:
        #TableHelpers.increasePercetnage = TableHelpers.Strategy
        #baseCounter = 0
        #while baseCounter <= 1:
        #settings.round += 10
        #TableHelpers.counting = baseCounter
        #settings.players = []
            #round = settings.round
            #shoe = settings.shoe
            #discarded = settings.discarded
            #cardsinshoe = shoe._cards
            #discarded = settings.discarded
            #region Logging
