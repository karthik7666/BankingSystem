from BankTransactions import Transactions
class ExistingUser:

    def ExistingCustomerOption(self,CustomerID):
        trans = Transactions()
        actiontobeperformed = int(input("Please choose option 1 for deposit 2 for Withdrawal and 3 to update personal information"))
        if actiontobeperformed == 1:
            trans.Deposit(CustomerID)
        elif actiontobeperformed == 2:
            trans.Withdrawal(CustomerID)
        else:
            trans.Updateprofile()
