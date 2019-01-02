USE [TestDB]
GO

/****** Object:  Table [dbo].[Accounts]    Script Date: 12/31/2018 3:07:33 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Accounts](
	[CustomerID] [int] NOT NULL,
	[AccountTypeId] [int] NOT NULL,
	[AccountId] [int] IDENTITY(1,1) NOT NULL,
	[accountnumber] [uniqueidentifier] NOT NULL,
	[balance] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[AccountId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[Accounts] ADD  CONSTRAINT [DF_accounts_accountnumber]  DEFAULT (newsequentialid()) FOR [accountnumber]
GO

ALTER TABLE [dbo].[Accounts] ADD  DEFAULT ((0)) FOR [balance]
GO


