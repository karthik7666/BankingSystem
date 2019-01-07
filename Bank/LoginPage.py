from BankingSystem.BankingSystem.Bank.BankTransactions import Transactions
from BankingSystem.BankingSystem.Bank.ExistingUser import ExistingUser
from WelcomeUser import UserInput
import hashlib, binascii, os
class Login:

    def UserLogin(self):

        print("Login to Banking System")
        prompt = int(input("Press 1 for Adminstrator or 2 for customer and further transactions \n"))
        CustomerID = int(input("Please enter your CustomerId \n"))
        Password = input("Please enter your password \n")
        if self.login(CustomerID, Password):
            if prompt == 1:
                print("Hello, Admisntrator. Welcome to Banking System")
                user = UserInput()
                user.bank()
            else:
                print("Hello, Banking User. Welcome to Banking System")
                ExistingUser().ExistingCustomerOption(CustomerID)
        else:
            print("Please enter correct Username/password.")


    def login(self, CustomerID, Providedpassword):
        trans = Transactions()
        getUsers_storedPassword = trans.GetPassword(CustomerID)
        if self.verify_password(getUsers_storedPassword, Providedpassword):
            return True
        else:
            return False


    def verify_password(self,stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

if __name__ == "__main__":
    login = Login()
    login.UserLogin()

