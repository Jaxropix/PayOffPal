from asyncio.windows_events import NULL
import CapitalOneAPI

class Loan:
    def __init__(self):
        self.id = ""
        self.creationDate = ""
        self.term = ""
        self.minPayment = 0
        self.amount = 0
        self.name = ""
        self.interestRate = 0
        self.interesttype = "fixed"
        self.status = ""

    def __str__(self):
        return f'Loan {self.id} is a {self.name} created on {self.createdDate}. The amount taken out is {self.amount} with a {self.interesttype} interest rate of {self.interestRate} to be paid off within {self.term} with a mean payment of {self.minPayment} each month'


    def GetLoan(id):
        return NULL

    def SetLoanData(loanData):
        print(loanData)
