from abc import ABC,abstractmethod

def InvalidBankException(Exception):

    def __init__(self,mesg):
        super().__init__(mesg)

def IsvalidCustomerException(Exception):

    def __init__(self,mesg):
        super().__init__(mesg)



class Bank(ABC):
    @abstractmethod
    def DepositAmount(self):
        pass


    @abstractmethod
    def WithdrawAmount(self):
        pass

    def checkIsValidCustomer(self,customer):
        if customer.cust_bankType == 'SBI' or customer.cust_bankType == 'HDFC' or customer.cust_bankType == 'ICICI':
            return True
        else:
            raise InvalidBankException('You are Enterd invalid Bank Type but you belongs to'+ customer.cust_bankType)


class SBI(Bank):
    sbiBalance = 10000
    listofpins = ['1234','4567','8910','9876','5432','1542']

    def __init__(self,customer):
        isValidCustomer = self.checkIsValidCustomer(customer)#Not Getting This Statement
        if isValidCustomer and SBI.listofpins.__contains__(customer.custAtmpin):
            customer.isValidCustomer = True #check it once
        else:
            customer.isValidCustomer = False

    def DepositAmount(self,customer,Depositamnt ):
        if customer.isValidCustomer :
            SBI.sbiBalance += Depositamnt
            customer.custbalance += Depositamnt
        else:
            raise InvalidBankException('You Are Not Belongs to SBI, Your Acc is in'+Customer.cust_bankType)

    def WithdrawAmount(self,customer,Withdrawamut):
        if customer.isValidCustomer:
            SBI.sbiBalance -= Withdrawamut
            customer.custbalance -= Withdrawamut


class Customer:

    def __init__(self,Name,Banktype,CustomerId,Atmpin,Balance,Account_type):
        self.custName = Name
        self.cust_bankType = Banktype
        self.custId = CustomerId
        self.custAtmpin = Atmpin
        self.custbalance = Balance
        self.Cust_Actype = Account_type


    def __str__(self):
        return 'Customer Name:{}\n' \
               'Customer Bank Type:{}\n' \
               'Customer ID:{}\n'\
               'Customer Atm Pin:{}\n'\
               'Customer Balance:{}\n'\
               'Customer Account Type:{}\n'.format(self.custName, self.cust_bankType,self.custId,self.custAtmpin,self.custbalance,self.Cust_Actype)

#Name,Banktype,CustomerId,Atmpin,Balance,Account_type
cust1 = Customer('Ashish','SBI',101,1234,5000,'Saving')
SBI.DepositAmount(cust1,Customer,5000)
print(cust1)
#DepositAmount=(cust1,500)
var1 = SBI.sbiBalance
print(var1)


'''
class HDFC(Bank):
    hdfcBalance = 100000
    listofpins = ['1234', '4567', '8910', '9876', '5432', '1542']

    def __init__(self, customer):
        isValidCustomer = self.checkIsValidCustomer(customer)  # Not Getting This Statement
        if isValidCustomer and HDFC.listofpins.__contains__(customer.pin):
            customer.isValidCustomer = True  # check it once
        else:
            customer.isValidCustomer = False

    def DepositAmount(self, Customer, Depositamnt):
        if Customer.isValidCustomer:
            HDFC.hdfcBalance += Depositamnt
            Customer.custbalance += Depositamnt
        else:
            raise InvalidBankException('You Are Not Belongs to SBI, Your Acc is in' + Customer.cust_bankType)

    def WithdrawAmount(self, Customer, Withdrawamut):
        if Customer.isValidCustomer:
           HDFC.hdfcBalance += 


class ICICI(Bank):

  '''



