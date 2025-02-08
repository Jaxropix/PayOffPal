import numpy_financial as npf
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
        self.interestPaymentPerTerm = 0
        self.principalPaymentPerTerm = 0
        self.additionalInformation = ""

    def __str__(self):
        return f'Loan {self.id} is a {self.name} created on {self.createdDate}. The amount taken out is {self.amount} with a {self.interesttype} interest rate of {self.interestRate} to be paid off within {self.term} with a mean payment of {self.minPayment} each month. {self.additionalInformation}'


    def GetLoan(id):
        return 

    def SetLoanData(self, loanData):

        # CalculateLoanInfo(loanData)
        # {
        #     "principalAmount" : "1500",
        #     "interestRatePrecentage" : "3",
        #     "termLength" : "24",
        #     "minimumPayment" : "40",
        #     "paidAmount" : ""
        # }

        return 


    def CalculateLoanData(principalAmount, minimumPayment, interestRate, termLength, amountPaid):
        return
        

