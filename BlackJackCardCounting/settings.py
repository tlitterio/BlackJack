def init():
    #RecordtoDbRound = 250
    global definition; definition = "Table Number: 16 - Scaled Counting"
    global betIncreaseFactor;betIncreaseFactor = 5
    global tableminimumbet;tableminimumbet = 25
    global tablemaximumbet;tablemaximumbet = 1000
    global decks;decks = 6
    global numberOfPlayers;numberOfPlayers = 2
    global genericplayersnewbies;genericplayersnewbies = 0
    global Strategy;Strategy = 3
    global dealerSoft17;dealerSoft17 = 0
    global increasePercetnage;increasePercetnage = 0
    global set;set = 1

    global WalkAway;WalkAway = 0
    global WalkAwayLoss;WalkAwayLoss = -1000
    global WalkAwayWinLimit;WalkAwayWinLimit = 2000
    global WalkAwayWinBigLimit;WalkAwayWinBigLimit = 3000
    global WalkAwayWin;WalkAwayWin = (.8) #of highest purse
    global WalkAwayWinBig;WalkAwayWinBig = (.9) #of highest purse

    global BaseCounter;BaseCounter = 1
    global counting;counting = 1
    global reshuffleDecks;reshuffleDecks = 1.5
    global reshuffleStDev;reshuffleStDev = None#.2
    global reshufflePercentage;reshufflePercentage = reshuffleDecks/decks
    global blackjackpayout;blackjackpayout = 3/2
    global discarded;discarded = []
    global players;players = []
    global cardsFaceValues;cardsFaceValues = 14
    global cardsSuitValues;cardsSuitValues = 4
    global dealersvisiblecardvalue;dealersvisiblecardvalue = 0
    global dealersScore;dealersScore = 0
    global fullDecklength;fullDecklength = decks*52

    global TablePrefix;TablePrefix = "v2.0Mit"
    global MasterId;MasterId= 1
    global TableNumber;TableNumber = 16
    global round;round = 1
    global realCount;realCount = 0.0
    global totalCountPercentage;totalCountPercentage = 0
    global shoe
    global drop;drop =1
    global debug;debug =1
    global SimulationId;SimulationId = TableNumber
