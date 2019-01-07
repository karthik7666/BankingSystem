from BankTransactions import Transactions
import hashlib, binascii, os
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
        self.Password = ""

    def AccountCreation(self):
        self._name = input("please enter your Name")
        self._custRole = input("Please enter 1 for Regional Manager , 2 for Branch Manager and 3 for User.")
        self._DOB = input("please enter your Date of birth")
        self._DateOfACccCreation = input("please enter your Date of Account Creation")
        self._Addrss = input("please enter your Address")
        self._Phno = input("please enter your Phone Number")
        self._adharcard = input("please enter your Aadhar card")
        self._pancard = input("please enter your Pancard")
        self._accounttype = input("Please enter your account type")
        self._branchname = input("please enter your Branch name")
        self.Password = self.hash_password(input("please enter your password"))
        trans = Transactions()
        trans.insertNewUser(self._Name,self._custRole,self._DOB,self._DateOfACccCreation,self._Addrss,self._Phno,self._adharcard,self._pancard,
                            self._accounttype,self._branchname,self.Password)

    def hash_password(self,password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

















