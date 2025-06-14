"""Assignment 3 Interest_update.py

The purpose of this program is to create a client service to apply interest based on their balance
"""

__author__ = "Ivan Estropigan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Dev Team, w3school, peps.python.org"

# importing pprint python built in
from pprint import pprint

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

        #key is the account number and value is $
        customers_account[key] = float(value)


    pprint(customers_account)
