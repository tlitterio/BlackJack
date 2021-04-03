import TableHelpers
import datetime
import urllib.parse
import pyodbc
import sqlalchemy as sa
import collections
from Classes.Simulations import Simulation
from Classes import Logs

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import Session

import settings
from settings import *
metadata = MetaData()

Base = declarative_base()
engine = None

global logLevel; logLevel = 1
global LogEntries; LogEntries = []
global RecordEntries; RecordEntries = []
global SimulationEntries; ConfigEntries = []
sa.text = "GETDATE()"


global connection
connectionString = "DRIVER={SQL Server Native Client 11.0};SERVER=SQLSERVER;DATABASE=BlackJackTesting;UID=BJ;PWD=P@ssword"
connectionString = urllib.parse.quote_plus(connectionString)
connectionString = "mssql+pyodbc:///?odbc_connect=%s" % connectionString

engine = sa.create_engine(connectionString) 
connection = engine.connect()
session = Session(bind=connection.engine)


def RecordSimulationData():
    from dill.source import getsource
    PayoutConfig = getsource(TableHelpers.CalculatePayouts)
    tempVar = Simulation(
        settings.counting,
        settings.reshufflePercentage,
        settings.reshuffleDecks,
        settings.numberOfPlayers,
        settings.tableminimumbet,
        settings.tablemaximumbet,
        settings.WalkAwayLoss,
        settings.WalkAwayWin,
        settings.WalkAwayWinLimit,
        settings.WalkAwayWinBig,
        settings.WalkAwayWinBigLimit,
        settings.players[0]._peakpurse,
        settings.CounterEndingPurse,
        settings.definition,
    )
    SimulationEntries.append(tempVar)

    #Main.main.drop(engine, checkfirst = True)
    #Main.main.create(engine, checkfirst = True)    
    #Classes.Records.Table.drop(engine)
    #Classes.Logs.Table.drop(engine)
    #Classes.Configs.Table.drop(engine)
    
    #Classes.Records.Table.create(engine)
    #Classes.Logs.Table.create(engine)
    #Classes.Configs.Table.create(engine)

def Log(id,round,log):
    TempLog = Logs.Log(id,round,log)
    LogEntries.append(TempLog)



def SerializeSimulation():
    def GetFinalPurses():
        peakcounter = None
        counter = None
        peakmoneybags= None
        moneybags= None
        for p in settings.players:
            if (p._label == "Counter"):
                counter = p._purse
                peakcounter = p._peakpurse
            if (p._label == "MoneyBags"):
                moneybags = p._purse
                peakmoneybags = p._peakpurse
        return (counter,peakcounter,moneybags,peakmoneybags)
    purses = GetFinalPurses()
    varConfig = Classes.Simulations.Simulation(
        settings.round,
        purses[1],
        purses[0],
        purses[3],
        purses[2],
        )
    SimulationEntries.append(varConfig)
    test = 0

def PostRounds():
    global connection
    connectionString = "DRIVER={SQL Server Native Client 11.0};SERVER=SQLSERVER;DATABASE=BlackJackTesting;UID=BJ;PWD=P@ssword"
    connectionString = urllib.parse.quote_plus(connectionString)
    connectionString = "mssql+pyodbc:///?odbc_connect=%s" % connectionString

    engine = sqlalchemy.create_engine(connectionString) 
    connection = engine.connect()
    dbWrite()
    connection.close()
    return

def dbWrite():
    LogEntries
    RecordEntries
    ConfigEntries
    if (logLevel <= 0): session.bulk_save_objects(ConfigEntries)
    if (logLevel <= 1): session.bulk_save_objects(RecordEntries)
    if (logLevel <= 2): session.bulk_save_objects(LogEntries)
    RecordEntries.clear()
    LogEntries.clear()
    ConfigEntries.clear()
    session.commit()

#def InitializeTables():
#    simulationstable.drop(engine, checkfirst = True)
#    simulationstable.create(engine, checkfirst = True)
#def SerializeRecords():
#    if (logLevel != 1): return
#    round = settings.round
#    shoe = settings.shoe
#    discarded = settings.discarded
#    fullDecklength = settings.fullDecklength
#    counting = settings.counting
#    for player in settings.players:
#        for h in player._hands:
#            counter = 0
#            for c in h._cards:
#                len(h._results)
#                ResultArray = ""
#                cindex = h._cards.index(c)
#                if cindex > 0:
#                    ResultArray = h._results[cindex]
#                ShoePercentage = len(shoe._cards)/fullDecklength
#                varRecord = Simulation(
#                            counting,
#                            settings.set,
#                            round,
#                            h._iteration,
#                            len(shoe._cards),
#                            len(discarded),
#                            player._label,
#                            player._purse,
#                            player._hands.index(h),
#                            h._algo,
#                            h._cards.index(c),
#                            h._split,
#                            h._sibling,
#                            h._score,
#                            c._cardFace,
#                            ResultArray,
#                            c._suitFace,
#                            c._value,
#                            c._index,
#                            h._result,
#                            shoe._totalcount,
#                            shoe._roundcount,
#                            shoe._percentagecount,
#                            shoe._percentagecountpreviousround,
#                            player._ibet,
#                            player._cbet,
#                            player._lastroundpayout
#                        )
#                RecordEntries.append(varRecord)
#                counter += 1
#region Garbage Collection
    #shoetable.create(engine, checkfirst = True)
    #shoetable.drop(engine, checkfirst = True)
    #name = "Shoes"
    #ShoesTableName=TablePrefix+str(TableNumber)+name
    #shoetable = Table(ShoesTableName, metadata,
    #    Column('Id',Integer, primary_key=True),
    #    Column('SimulationId',Integer,  ForeignKey(SimulationsTableName+".Id")),
    #    Column('RoundId',Integer,  ForeignKey(RoundsTableName+".Id")),
    #    Column('ShoePercent',Float),
    #    Column('ShoePercentPreviousRound',Float),
    #    Column('ReshuffleRemaining',Integer),
    #    Column('TimeStamp',DateTime,server_default=sa.text),
    #)
    #mapper(Shoes.Shoe,shoetable)

#simnulationsame = "Simulations"
#SimulationsTableName=TablePrefix+simnulationsame
#simulationstable = Table(SimulationsTableName, metadata,
#    Column('Id',Integer, primary_key=True),
#    Column('Strategy',Integer),
#    Column('TotalRounds',Integer),
#    Column('Counting',Integer),
#    Column('ReshufflePercentage',Float),
#    Column('ReshuffleMean',Float),
#    Column('ReshuffleStDev',Float),
#    Column('NumberOfPlayers',Integer),
#    Column('GenericPlayersNewbies',Integer),
#    Column('BetIncreaseFactor',Integer),
#    Column('MinBet',Float),
#    Column('MaxBet',Float),
#    Column('WalkAwayLoss',Float),
#    Column('WalkAwayWinLimit',Float),
#    Column('WalkAwayWin',Float),
#    Column('CounterPeakPurse',Float),
#    Column('CounterEndingPurse',Float),
#    Column('MoneyBagsPeakPurse',Float),
#    Column('MoneyBagsEndingPurse',Float),
#    Column('DealerSoft17',Integer),
#    Column('TimeStamp',DateTime,server_default=sa.text),
#)

#playersname = "Players"
#PlayersTableName=TablePrefix+str(TableNumber)+playersname
#playerstable = Table(PlayersTableName, metadata,
#    Column('Id',Integer, primary_key=True),
#    Column('SimulationId',Integer, ForeignKey(SimulationsTableName+".Id")),
#    Column('Label',String),
#    Column('Active',Integer),
#    Column('Purse',Float),
#    Column('PeakPurse',Float),
#    Column('LastRoundPayout',Float),
#    Column('InitialBet',Float),
#    Column('CurrentBet',Float),
#    Column('Result',String),
#    Column('TimeStamp',DateTime,server_default=sa.text),
#)

#roundsname = "Rounds"
#RoundsTableName=TablePrefix+str(TableNumber)+roundsname
#roundstable = Table(RoundsTableName, metadata,
#    Column('Id',Integer, primary_key=True),
#    Column('SimulationId',Integer, ForeignKey(SimulationsTableName+".Id")),
#    Column('PlayerId',Integer,  ForeignKey(PlayersTableName+".Id")),
#    Column('Counting',Integer),
#    Column('Round',Integer),
#    Column('Iteration',Integer),
#    Column('Shoe',Integer),
#    Column('Discarded',Integer),
#    Column('Player',String),
#    Column('Purse',Integer),
#    Column('Hand',Integer),
#    Column('Algo',Integer),
#    Column('Card',Integer),
#    Column('Split',Integer),
#    Column('Sibling',Integer),
#    Column('Score',Integer),
#    Column('CardFace',String),
#    Column('ResultArray',String),
#    Column('CardSuit',String),
#    Column('CardValue',Integer),
#    Column('CardIndex',Integer),
#    Column('Result',String),
#    Column('TotalCount',Integer),
#    Column('RoundCount',Integer),
#    Column('ShoePercent',Float),
#    Column('ShoePercentPreviousRound',Float),
#    Column('InitBet',Integer),
#    Column('CurrentBet',Integer),
#    Column('Payout',Float),
#    Column('TimeStamp',DateTime,server_default=sa.text),
#)

    #    import sqlalchemy as sa
    #from sqlalchemy.ext.declarative import declarative_base
    #from sqlalchemy.orm import mapper
    #from sqlalchemy import (Table, 
    #                        Column, 
    #                        Integer, 
    #                        String, 
    #                        MetaData, 
    #                        ForeignKey, 
    #                        Float, 
    #                        DateTime)
    #metadata = MetaData()
    #from Classes import Cards, Hands, Rounds, Players, Simulations, Logs, Shoes
    #sa.text = "GETDATE()"

    #name = "Simulations"
    #SimulationsTableName=TablePrefix+name
    #simulationstable = Table(SimulationsTableName, metadata,
    #    Column('Id',Integer, primary_key=True),
    #    Column('Strategy',Integer),
    #    Column('TotalRounds',Integer),
    #    Column('Counting',Integer),
    #    Column('ReshufflePercentage',Float),
    #    Column('ReshuffleMean',Float),
    #    Column('ReshuffleStDev',Float),
    #    Column('NumberOfPlayers',Integer),
    #    Column('GenericPlayersNewbies',Integer),
    #    Column('BetIncreaseFactor',Integer),
    #    Column('MinBet',Float),
    #    Column('MaxBet',Float),
    #    Column('WalkAwayLoss',Float),
    #    Column('WalkAwayWinLimit',Float),
    #    Column('WalkAwayWin',Float),
    #    Column('CounterPeakPurse',Float),
    #    Column('CounterEndingPurse',Float),
    #    Column('MoneyBagsPeakPurse',Float),
    #    Column('MoneyBagsEndingPurse',Float),
    #    Column('DealerSoft17',Integer),
    #    Column('TimeStamp',DateTime,server_default=sa.text),
    #)
    ##mapper(Simulations.Simulation,simulationstable)

    #name = "Players"
    #PlayersTableName=TablePrefix+str(TableNumber)+name
    #playerstable = Table(PlayersTableName, metadata,
    #    Column('Id',Integer, primary_key=True),
    #    Column('SimulationId',Integer, ForeignKey(SimulationsTableName+".Id")),
    #    Column('Label',String),
    #    Column('Active',Integer),
    #    Column('Purse',Float),
    #    Column('PeakPurse',Float),
    #    Column('LastRoundPayout',Float),
    #    Column('InitialBet',Float),
    #    Column('CurrentBet',Float),
    #    Column('Result',String),
    #    Column('TimeStamp',DateTime,server_default=sa.text),
    #)
    ##mapper(Players.Player,playerstable)

    #name = "Rounds"
    #RoundsTableName=TablePrefix+str(TableNumber)+name
    #roundstable = Table(RoundsTableName, metadata,
    #    Column('Id',Integer, primary_key=True),
    #    Column('SimulationId',Integer, ForeignKey(SimulationsTableName+".Id")),
    #    Column('PlayerId',Integer,  ForeignKey(PlayersTableName+".Id")),
    #    Column('Counting',Integer),
    #    Column('Round',Integer),
    #    Column('Iteration',Integer),
    #    Column('Shoe',Integer),
    #    Column('Discarded',Integer),
    #    Column('Player',String),
    #    Column('Purse',Integer),
    #    Column('Hand',Integer),
    #    Column('Algo',Integer),
    #    Column('Card',Integer),
    #    Column('Split',Integer),
    #    Column('Sibling',Integer),
    #    Column('Score',Integer),
    #    Column('CardFace',String),
    #    Column('ResultArray',String),
    #    Column('CardSuit',String),
    #    Column('CardValue',Integer),
    #    Column('CardIndex',Integer),
    #    Column('Result',String),
    #    Column('TotalCount',Integer),
    #    Column('RoundCount',Integer),
    #    Column('ShoePercent',Float),
    #    Column('ShoePercentPreviousRound',Float),
    #    Column('InitBet',Integer),
    #    Column('CurrentBet',Integer),
    #    Column('Payout',Float),
    #    Column('TimeStamp',DateTime,server_default=sa.text),
    #)
    ##mapper(Rounds.Round,roundstable)


    #name = "Hands"
    #HandsTableName=TablePrefix+str(TableNumber)+name
    #handstable = Table(HandsTableName, metadata,
    #    Column('Id',Integer, primary_key=True),
    #    Column('SimulationId',Integer,  ForeignKey(SimulationsTableName+".Id")),
    #    Column('PlayerId',Integer,  ForeignKey(PlayersTableName+".Id")),
    #    Column('RoundId',Integer,  ForeignKey(RoundsTableName+".Id")),
    #    Column('Cards',Integer),
    #    Column('Set',Integer),
    #    Column('Round',Integer),
    #    Column('Iteration',Integer),
    #    Column('Shoe',Integer),
    #    Column('Discarded',Integer),
    #    Column('Player',String),
    #    Column('Purse',Integer),
    #    Column('Hand',Integer),
    #    Column('Algo',Integer),
    #    Column('Card',Integer),
    #    Column('Split',Integer),
    #    Column('Sibling',Integer),
    #    Column('Score',Integer),
    #    Column('CardFace',String),
    #    Column('ResultArray',String),
    #    Column('CardSuit',String),
    #    Column('CardValue',Integer),
    #    Column('CardIndex',Integer),
    #    Column('Result',String),
    #    Column('TotalCount',Integer),
    #    Column('RoundCount',Integer),
    #    Column('ShoePercent',Float),
    #    Column('ShoePercentPreviousRound',Float),
    #    Column('InitBet',Integer),
    #    Column('CurrentBet',Integer),
    #    Column('Payout',Float),
    #    Column('TimeStamp',DateTime,server_default=sa.text),
    #)
    ##mapper(Hands.Hand,handstable)

    #name = "Cards"
    #CardsTableName=TablePrefix+str(TableNumber)+name
    #cardstable = Table(CardsTableName, metadata,
    #    Column('Id',Integer, primary_key=True),
    #    Column('SimulationId',Integer,  ForeignKey(SimulationsTableName+".Id")),
    #    Column('PlayerId',Integer,  ForeignKey(PlayersTableName+".Id")),
    #    Column('RoundId',Integer,  ForeignKey(RoundsTableName+".Id")),
    #    Column('HandId',Integer,  ForeignKey(HandsTableName+".Id")),
    #    Column('ShoePercent',Float),
    #    Column('ShoePercentPreviousRound',Float),
    #    Column('ReshuffleRemaining',Integer),
    #    Column('TimeStamp',DateTime,server_default=sa.text),
    #)
    ##mapper(Cards.Card,cardstable)

    #name = "Logs"
    #LogsTableName=TablePrefix+str(TableNumber)+name
    #logstable = Table(LogsTableName, metadata,
    #    Column('Id',Integer, primary_key=True),
    #    Column('SectionId',Integer),
    #    Column('Set',Integer),
    #    Column('Round',Integer),
    #    Column('Log',String),
    #    Column('TimeStamp',DateTime,server_default=sa.text),
    #    )
    #mapper(Logs.Log,logstable)

#endregion
