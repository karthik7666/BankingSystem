USE [TestDB]
GO

/****** Object:  Trigger [dbo].[trig_Update_Customer]    Script Date: 12/31/2018 3:20:35 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TRIGGER [dbo].[trig_Update_Customer]
ON [dbo].[Customers]
FOR INSERT
AS
Begin
    Insert into Accounts(CustomerID, AccountTypeId) 
    select c.customerID, at.accounttypeID from inserted c inner join dbo.Accounttype at 
on c.Accounttype = at.accounttype where c.customerID = (select max(customerID) from customers)
End
GO


