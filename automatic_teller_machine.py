"""Assignment 3"""

__author__ = "Ivan Estropigan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Dev Team, w3school, peps.python.org"

import random
import os
from time import sleep

#Variables
menu_options = {"deposit": "D", "withdraw": "W", "quit": "Q"}
user_options = ""
balance = random.uniform(-1000, 10000)

max_width = "*" * 40
text_pixell_river_financial = "PIXELL RIVER FINANCIAL".center(40)
text_atm_simulator = "ATM Simulator".center(40)
text_invalid = "INVALID SELECTION".center(40)
text_insufficient = "INSUFFICIENT FUNDS".center(40)
"""
Prints the output of the ATM User interface

Args:
menu_options = {"deposit": "D", "withdraw": "W", "quit": "Q"}
balance = random.uniform(-1000, 10000)

max_width = "*" * 40 
text_pixell_river_financial = "PIXELL RIVER FINANCIAL".center(40)
text_atm_simulator = "ATM Simulator".center(40)

text_invalid = "INVALID SELECTION".center(40)

Returns:
**************************************** 
             ATM Simulator

   Your Current balance is: $4267.94
               Deposit: D
              Withdraw: W
                Quit: Q
****************************************
"""


text_balance = f"Your Current balance is: ${balance:.2f}".center(40)
text_deposit = "Deposit: D".center(40)
text_widthdraw = "Withdraw: W".center(40)
text_quit = "Quit: Q".center(40)

print(f"{max_width} \n"
      f"{text_pixell_river_financial} \n"
      f"{text_atm_simulator}\n"
      f"\n{text_balance}"
      f"\n{text_deposit}"
      f"\n{text_widthdraw}"
      f"\n{text_quit}"
      f"\n{max_width}")

user_options = input("Enter your selection: ").upper()

# .values is the value inside the key(d,w,q)
if user_options not in menu_options.values():
    print(f"{max_width}"
          f"\n{text_invalid}"
          f"\n{max_width}")

# when user presses D transaction amount will be added
elif user_options == 'D':
    transaction = float(input("Enter your transaction amount: "))
    balance += transaction
    print(f"{max_width}"
          f"\nYour current balance is: {balance:.2f}"
          f"\n{max_width}")

# when user presses w check first if user transaction > balance
elif user_options == 'W':
    transaction = float(input("Enter your transaction amount: "))
    if transaction > balance:
        print(f"{max_width}"
              f"\n{text_insufficient}"
              f"\n{max_width}")
 
# if balance is sufficient subtract transaction to balance.
    else:
        balance -= transaction
        print(f"{max_width}"
          f"\nYour current balance is: {balance:.2f}"
          f"\n{max_width}")
