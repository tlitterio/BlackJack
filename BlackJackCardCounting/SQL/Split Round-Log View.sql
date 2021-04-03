USE [BlackJackTesting]
GO

/****** Script for SelectTopNRows command from SSMS  ******/
DECLARE @r int
set @r = 4
SELECT *
  FROM [BlackJackTesting].[dbo].[Log3]
  WHERE [Round] = @r
  ORDER BY Id DESC


SELECT *,Shoe+Discarded as TotalCards
FROM [BlackJackTesting].[dbo].[Game3]
WHERE [Round] = @r
ORDER BY Id DESC
