import CapitalOneAPI
import sys

if sys.platform == "win32":
    from asyncio.windows_events import NULL
else:
    NULL = None 

import CapitalOneAPI
import os
import numpy_financial as np



class Loan:
    def __init__(self):
        self.id = ""
        self.creationDate = ""
        self.term = 0
        self.minPayment = 0
        self.amount = 0
        self.originalLoan = 0
        self.interestRate = 0.0
        self.interestPaidPerTerm = 0
        self.principalPaidPerTerm = 0
        self.interesttype = "fixed"
        self.status = ""
        self.additionalInformation = ""

    def __str__(self):
        return f'Loan {self.id} is a {self.name} created on {self.createdDate}. The amount taken out is {self.amount} with a {self.interesttype} interest rate of {self.interestRate} to be paid off within {self.term} with a mean payment of {self.minPayment} each month. {self.additionalInformation}'

    def string_to_int(self, s):
        if s is None:
            return 0
        try:
            return int(s)
        except ValueError:
            return 0

    def GetLoan(self):
        loanId = os.getenv("LOAN_ID")
        loanData = CapitalOneAPI.GetCapitalOneLoanById(loanId)

        monthlyPayment = loanData["monthly_payment"]
        term = loanData["description"].split(",")

        return { "montly_payment" : monthlyPayment, "term_length" : term[1] }

    def SetLoanData(self, loanData):
        principal = int(loanData["principalAmount"])
        term_length = int(loanData["termLength"])
        interest_rate = int(loanData["interestRatePrecentage"])
        min_payment = int(loanData["minimumPayment"])
        paid = self.string_to_int(loanData["principalAmount"])
        creationDate = loanData["creationDate"]

        
        monthly_rate = (interest_rate / 100) / 12
        remaining_principal = principal - paid

        self.creationDate = creationDate
        self.status = "pending"

        self.CalculateLoanInfo(interest_rate, principal, term_length, paid, min_payment)
        
        metadata = f"{self.amount},{self.term},{self.interestRate},{self.interestPaidPerTerm},{self.principalPaidPerTerm}"

        loanId = CapitalOneAPI.CreateCapitalOneLoan(self.status, 650, min_payment, self.originalLoan, metadata)
        os.environ["LOAN_ID"] = loanId
        

    def CalculateLoanInfo(self,interest_rate, principal, term_length, paid, minPayment):
        monthly_rate = (interest_rate / 100) / 12
        remaining_principal = principal - paid

        monthly_payment = np.fv(monthly_rate, term_length, 0, -remaining_principal) / term_length
        interest_paid = remaining_principal * monthly_rate
        principal_paid = monthly_payment - interest_paid

        if minPayment < monthly_payment:
            self.additionalInformation = "In order to pay off your loan in the stated time, you might need to make a little more in monthly payments"

        self.minPayment = 45
        self.interestPaidPerTerm = 15
        self.principalPaidPerTerm = 30
        self.term = term_length
        self.amount = 45 * term_length
        self.originalLoan = principal
        self.interestRate = interest_rate

    