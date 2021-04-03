#import Players
#import Hands
#import Cards
#import random

##region Global Variable Initialization
##global db; db = 0
#global Testing; Testing = 0

#global Decks; Decks = 4
#global TotalNumIndCards;TotalNumIndCards = Decks*4 #Number of each individual cards based on #of Decks time 4 suits

#global MinimumBet; MinimumBet = 5
#global MaximumBet; MaximumBet =100

#global NumberOfAddPlayers; NumberOfAddPlayers = 0 #Over the initial Player/Dealer e.g. a 1 would intiiate a game between the counter and dealer with one addiitonal player at the table
#global PlayerPurse; PlayerPurse = 100
#global PlayerInitialBet; PlayerInitialBet = MinimumBet

##endregion

##region Explanation
#    #NumberOfPlayers is defined as the number of General Players at the table

#    #Strategy is defined as Follows:
#    #0=one on one between dealer and counter; no counting; baseline
#    #1=one on one between dealer and counter; counting
#    #2=dealer,counter and better; counting

#    #Players are defined as follows:
#    #n=Dealer; last number; makes it easy for dealing since the dealer deals last
#    #0=Counter - Player keeping count
#    #1=Better - if using the strategy for signaling a third party to the table to bet big
#    #2<n-1<n=General Player - Noise at the table; no counting; not invoved

#    #Assumption: All increase in betting will begin on the next round
##endregion

