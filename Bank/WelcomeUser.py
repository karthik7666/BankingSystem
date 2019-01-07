from NewUser import NewUser

class UserInput:

    def bank(self):
        prompt = int(input("Press 1 for New account creation with Zero balance or 2 for adding or updating bank Details \n"))

        if prompt == 1:
            cus = NewUser().AccountCreation()
        else:
            cus = ExistingUser().ExistingCustomerOption()



