from datetime import date
import os
import Loan



checkLoan = Loan.Loan()

creation = date.today().strftime("%Y-%m-%d")
test_data = {"principalAmount":"1500","interestRatePrecentage":"3","termLength":"24","minimumPayment":"40","paidAmount":"", "creationDate" : creation}
checkLoan.SetLoanData(test_data)
print(os.getenv("LOAN_ID"))

print(checkLoan.GetLoan())