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
