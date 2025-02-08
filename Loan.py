class Loan:
    def __init__(self, id, creationDate, minPayment, term, amount, name, rate):
        self.id = id
        self.creationDate = creationDate
        self.term = term
        self.minPayment = minPayment
        self.amount = amount
        self.name = name
        self.interestRate = rate
        self.interesttype = "fixed"

    def __str__(self):
        return f'Loan {self.id} is a {self.name} created on {self.createdDate}. The amount taken out is {self.amount} with a {self.interesttype} interest rate of {self.interestRate} to be paid off within {self.term} with a mean payment of {self.minPayment} each month'