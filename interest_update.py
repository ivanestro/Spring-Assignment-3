"""Assignment 3 Interest_update.py

The purpose of this program is to create a client service to apply interest based on their balance
"""

__author__ = "Ivan Estropigan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Dev Team, w3school, peps.python.org, stackoverflow"

# importing python built in pprint
from pprint import pprint

# importing csv
import csv


# Storing data from account_balances.txt
customers_account = {}

# open account_balances.txt, read a filler name ivan
with open("account_balances.txt", "r") as ivan:
    # loops each line on account balances
    for line in ivan:
        # key and value is account and value
        # line strip is removing the \n or white spaces
        # .split is splitting data into two parts
        key, value = line.strip().split("|")

        # update data key is the account number and value is $
        customers_account[key] = float(value)

    # updated print customer account
    print("Balance without interest: ")
    pprint(customers_account)

# checking inside the items of acc balances
for key, value in customers_account.items():
    
    # if value is less than 0:
    if value < 0:
        monthly_interest = value * -0.10
    
    # if value is less than < 1000
    elif value < 1000:
        monthly_interest = value * 0.01
    
    # if value is less than 5000
    elif value < 5000:
        monthly_interest = value * 0.025

    # else 5000 and above is 5% interest
    else:
        monthly_interest = value * 0.05
    
    # update the customer account by interest
    customers_account[key] = value + monthly_interest

# print to state balance with interest
print("\nBalance with interest: ")

# pprint the balance + interest
pprint(customers_account)

# Question 4 Save Updated Account Data
# assigning a name to new file
file_name = "updated_balances_IE.csv"

# this is to open the file, write
# new line is to not leave blank lines
# temporary name as update_ivan:
with open(file_name, "w", newline='') as update_ivan:
    # csv.writer is to create a row in csv file
    writer = csv.writer(update_ivan)
    # creating a header for account, balance
    writer.writerow(["Account", "Balance"])
    
    # gathering data within account, balance
    # get customers_account items the list in dictionary
    # basically writes its desired location
    # for each pair goes by their own line format.
    for Account, Balance in customers_account.items():
        writer.writerow((Account, Balance))

# Question 5

with open(file_name, "r")as update_ivan:
    reader = csv.DictReader(update_ivan)

    print("\nQuestion 5")
    for row in reader:
        print(row)