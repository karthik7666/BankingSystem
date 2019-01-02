from SimpleBankProject.Utility.DatabaseConnection import DBConnection
import datetime
from time import gmtime, strftime
class Transactions:

    def __init__(self):
        self.db = DBConnection()

    def insertNewUser(self,Name,CustRole,DOB,DateOfAccCreation,Addrss,Phno,adharcard,pancard,Accounttype,branchname):
        query = "INSERT INTO [dbo].[Customers] ([CustomerName],[CustomerRole],[DateofBirth],[DateofAccCreation],[Address],[PhoneNumber],[AadharNumber]," \
                "[Pancard],[Accounttype],[BranchName]) values (?,?,?,?,?,?,?,?,?,?)"

        val = (Name,CustRole,DOB,DateOfAccCreation,Addrss,Phno,adharcard,pancard,Accounttype,branchname)
        self.db.connect(query,val)

    def Deposit(self,CustomerID):
        DepositAmnt = int(input("Please enter the amount to be deplosited"))
        query = ("select Balance from accounts where customerId = ?")
        getaccountdetails = self.db.FetchResult(query,CustomerID)
        getaccountdetails += DepositAmnt
        self.TransactionCredit(CustomerID,DepositAmnt)
        self.TransactionUpdate(getaccountdetails,CustomerID)


    def Withdrawal(self,CustomerID):
        WithDrawAmnt = int(input("Please enter the amount you wish to withdraw"))
        query = ("select Balance from accounts where customerId = ?")
        getaccountdetails = self.db.FetchResult(query,CustomerID)
        getaccountdetails = getaccountdetails - WithDrawAmnt
        self.TransactionDebit(CustomerID,WithDrawAmnt)
        self.TransactionUpdate(getaccountdetails,CustomerID)

    def TransactionCredit(self,CustomerID,DepositAmnt):
        query = ("Insert into transactions (CustomerID,AccountID,TransactionDescription,CreditAmount,timeofTransaction)" 
                 "values ((select customerID from Accounts where CustomerID =?),(select AccountID from Accounts where CustomerID =?),?,?,?)")
        val = (CustomerID,CustomerID,"Credited amount",DepositAmnt,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.db.connect(query,val)

    def TransactionDebit(self,CustomerID,DepositAmnt):
        query = ("Insert into transactions (CustomerID,AccountID,TransactionDescription,DebitAmount,timeofTransaction)" 
                 "values ((select customerID from Accounts where CustomerID =?),(select AccountID from Accounts where CustomerID =?),?,?,?)")
        val = (CustomerID,CustomerID,"Debited amount",DepositAmnt,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.db.connect(query,val)

    def TransactionUpdate(self,Balanace,CustomerID):
        updatequery = ("update Accounts set Balance = ? where customerID = ?")
        updateval = (Balanace, CustomerID)
        self.db.connect(updatequery,updateval)
