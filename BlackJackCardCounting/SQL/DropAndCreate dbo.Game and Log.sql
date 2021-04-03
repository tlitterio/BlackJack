USE [BlackJackTesting]
GO
DECLARE @CreateSQL nvarchar(max), @DropSQL nvarchar(max)
DECLARE @GameTable nvarchar(100), @LogTable nvarchar(100)
DECLARE @Game nvarchar(10)

set @Game = '10'
set @GameTable = 'Mit' + @Game + 'Records'
set @LogTable = 'Mit' + @Game + 'Logs'

set @DropSQL = '
DROP TABLE [dbo].' + @GameTable + '
DROP TABLE [dbo].' + @LogTable+ '
'

set @CreateSQL = '
CREATE TABLE [dbo].' + @GameTable + ' (
    [Id]          INT           IDENTITY (1, 1) NOT NULL,
    [Round]       INT           NULL,
    [Iteration]   INT           NULL,
    [Shoe]        INT           NULL,
    [Discarded]   INT           NULL,
    [Player]      VARCHAR (10) NULL,
    [Purse]       MONEY    NULL,
    [Hand]        INT           NULL,
    [Algo]        INT           NULL,
    [Card]        INT           NULL,
    [Split]       INT           NULL,
    [Sibling]     INT           NULL,
    [Score]       INT           NULL,
    [CardFace]    VARCHAR (8) NULL,
    [ResultArray] VARCHAR (40) NULL,
    [CardSuit]    VARCHAR (8) NULL,
    [CardValue]   INT           NULL,
    [CardIndex]   INT           NULL,
    [Result]      VARCHAR (20) NULL,
    [TotalCount]   INT           NULL,
    [RoundCount]  INT           NULL,
    [ShoePercent] FLOAT (53)    NULL,
    [InitBet]     MONEY           NULL,
    [CurrentBet]  MONEY           NULL,
    [Payout]      MONEY		    NULL
);
CREATE TABLE [dbo].' + @LogTable + ' (
    [Id]        INT           IDENTITY (1, 1) NOT NULL,
    [Round]     INT           NULL,
    [SectionId] INT           NULL,
    [Log]       VARCHAR (500) NULL,
    [TimeStamp] datetime	  NULL
);
'

EXEC sp_executesql @DropSQL
EXEC sp_executesql @CreateSQL