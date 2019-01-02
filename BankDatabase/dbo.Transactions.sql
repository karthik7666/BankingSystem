USE [TestDB]
GO

/****** Object:  Table [dbo].[Transactions]    Script Date: 12/31/2018 3:19:37 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Transactions](
	[CustomerId] [int] NOT NULL,
	[AccountId] [int] NOT NULL,
	[TransactionDescription] [varchar](50) NULL,
	[DebitAmount] [money] NULL,
	[CreditAmount] [money] NULL,
	[TransactionId] [int] IDENTITY(1,1) NOT NULL,
	[timeofTransaction] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[TransactionId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


