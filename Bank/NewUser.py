from BankTransactions import Transactions
class NewUser:

    def __init__(self):
        self._Name =""
        self._custRole = ""
        self._DOB = ""
        self._DateOfACccCreation = ""
        self._Addrss = ""
        self._Phno = ""
        self._adharcard = ""
        self._pancard = ""
        self._accounttype = ""
        self._branchname = ""

    def AccountCreation(self):
        self._name = input("please enter your Name")
        self._custRole = input("Please enter 1 for User role and 2 for Bank Employee")
        self._DOB = input("please enter your Date of birth")
        self._DateOfACccCreation = input("please enter your Date of Account Creation")
        self._Addrss = input("please enter your Address")
        self._Phno = input("please enter your Phone Number")
        self._adharcard = input("please enter your Aadhar card")
        self._pancard = input("please enter your Pancard")
        self._accounttype = input("Please enter your account type")
        self._branchname = input("please enter your Branch name")
        trans = Transactions()
        trans.insertNewUser(self._Name,self._custRole,self._DOB,self._DateOfACccCreation,self._Addrss,self._Phno,self._adharcard,self._pancard,self._accounttype,self._branchname)



















