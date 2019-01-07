USE [TestDB]
GO

/****** Object:  Table [dbo].[UserRoles]    Script Date: 1/7/2019 12:59:17 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[UserRoles](
	[Role] [varchar](50) NOT NULL,
	[RoleID] [int] IDENTITY(1,1) NOT NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


