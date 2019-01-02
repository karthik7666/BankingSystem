from NewUser import NewUser
from SimpleBankProject.Bank.ExistingUser import ExistingUser
class UserInput:

    def bank():
        print("welcome")
        prompt = int(input("Press 1 for New account creation with Zero balance or 2 for existing customer and further transactions \n"))

        if prompt == 1:
            cus = NewUser().AccountCreation()
        else:
            cus = ExistingUser().ExistingCustomerOption()

    if __name__ == "__main__":
        bank()


