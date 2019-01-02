from BankTransactions import Transactions
class ExistingUser:

    def ExistingCustomerOption(self):
        accntNumber = input("Please enter your account number")
        trans = Transactions()
        actiontobeperformed = int(input("Please choose option 1 for deposit 2 for Withdrawal and 3 to update personal information"))
        if actiontobeperformed == 1:
            trans.Deposit(accntNumber)
        elif actiontobeperformed == 2:
            trans.Withdrawal(accntNumber)
        else:
            trans.Updateprofile()
