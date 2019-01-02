USE [TestDB]
GO

/****** Object:  Table [dbo].[Customers]    Script Date: 12/31/2018 3:18:55 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Customers](
	[CustomerName] [varchar](50) NOT NULL,
	[CustomerRole] [int] NOT NULL,
	[DateOfBirth] [date] NOT NULL,
	[DateofAccCreation] [date] NOT NULL,
	[Address] [varchar](50) NOT NULL,
	[PhoneNumber] [nvarchar](50) NULL,
	[AadharNumber] [varchar](50) NULL,
	[Pancard] [varchar](50) NULL,
	[CustomerID] [int] IDENTITY(1,1) NOT NULL,
	[Accounttype] [varchar](50) NOT NULL,
	[Branchname] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[CustomerID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


