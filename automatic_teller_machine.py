"""Assignment 3"""

__author__ = "Ivan Estropigan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Dev Team, w3school, peps.python.org, stackoverflow, doc.python.org"

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

# While loop for user option if q is not pressed
while user_options != 'Q':
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    text_balance = f"Your Current balance is: ${balance:.2f}".center(40)
    text_deposit = "Deposit: D".center(40)
    text_withdraw = "Withdraw: W".center(40)
    text_quit = "Quit: Q".center(40)

    print(f"{max_width} \n"
      f"{text_pixell_river_financial} \n"
      f"{text_atm_simulator}\n"
      f"\n{text_balance}"
      f"\n{text_deposit}"
      f"\n{text_withdraw}"
      f"\n{text_quit}"
      f"\n{max_width}")
    """
    while user_option does not equal to Q then print  the required prompt 
    for the bank such as boarder, balance, deposit, withdraw, quit.
    """



    # user options regarding the menu options selection
    # .upper() this is to prevent users from getting errors
    user_options = input("Enter your selection: ").upper()


    # .values is the menu_option inside the key(d,w,q)
    if user_options not in menu_options.values():
        print(f"{max_width}"
              f"\n{text_invalid}"
              f"\n{max_width}")
        
        # Pause the script for the specified number of seconds
        sleep(2)

    # when user presses D transaction amount will be added
    # deposit an amount and add to the account
    elif user_options == 'D':
        transaction = float(input("Enter your transaction amount: "))
        balance += transaction
        print(f"\n{max_width}"
              f"\nYour current balance is: {balance:.2f}"
              f"\n{max_width}")
        
        # Pause the script for the specified number of seconds
        sleep(3)

    # when user presses w check first if user transaction > balance
    # if transaction is bigger then output insuff funds to the user
    elif user_options == 'W':
        transaction = float(input("Enter your transaction amount: "))
        if transaction > balance:
            print(f"{max_width}"
                  f"\n{text_insufficient}"
                  f"\n{max_width}")
            # Pause the script for the specified number of seconds
            sleep(3)

        # else transaction is valid then subtract it from bank
        else:
            balance -= transaction
            print(f"\n{max_width}"
                  f"\nYour current balance is: {balance:.2f}"
                  f"\n{max_width}")
            
            # Pause the script for the specified number of seconds
            sleep(3)

# Clear the program inside the infinite loop
os.system('cls' if os.name == 'nt' else 'clear')

# When Q is pressed then system shuts down
print("Program is Shutting down ")