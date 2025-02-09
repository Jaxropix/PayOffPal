import os
from urllib import response
import requests
from datetime import date
import json
from dotenv import load_dotenv 
load_dotenv() 

customerId = os.getenv("Customer_ID")
accountId = os.getenv("Account_ID")
apiKey = os.getenv("API_KEY")

def CreateCapitalOneLoan(status, creditScore, monthlyPayment, amount, metadata):

    createURLTemplate = os.getenv("Create_Endpoint")
    url = createURLTemplate.format(accountId=accountId, key=apiKey)

    payload = {
        "type" : "home",
        "status" : status,
        "credit_score" : creditScore,
        "monthly_payment": monthlyPayment,
        "amount" : amount,
        "description" : metadata
    }

    response = requests.post(
        url,
        data=json.dumps(payload),
        headers={'content-type' : 'application/json' }
        )

    
    if response.status_code == 201:
        print('account created')

    responseDictionary = response.json()
    print(response.json())
    return responseDictionary['objectCreated']['_id']

    


def FindCustomer():
    url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customerId,apiKey)

    response = requests.get(
        url,
        headers={'content-type' : 'application/json' }
        )

    print(response.status_code)


def FindAccount():
    url = 'http://api.nessieisreal.com/accounts/{}?key={}'.format(accountId,apiKey)

    response = requests.get(
        url,
        headers={'content-type' : 'application/json' }
        )

    print(response.status_code)

def GetCapitalOneLoanById(loanId):
    getLoanURLTemplate = os.getenv("GetLoan_Endpoint")
    url = getLoanURLTemplate.format(loanId, apiKey)

    
    response = requests.get(
        url,
        headers={'content-type' : 'application/json' }
        )

    return response.json()
