# Assignment 3

## Author

Ivan Estropigan

## Contents

- [Description](#description)
- [Assignment Instructions](#assignment-instructions)
- [ATM Simulator Requirements](#atm-simulator-requirements)
- [Update README File](#1-update-the-readme-file)
- [Define User Interface](#2-define-user-interface)
- [Processes Transaction](#3-processes-transactions)
- [Incorporate Multiple Transactions](#4-incorporate-multiple-transactions)
- [Source Code Review](#5-source-code-review)
- [Interest Update Requirements](#interest-update-requirements)
- [Update The README File](#update-the-readme-file)
- [Print Customer Balances](#2-print-customer-balances)
- [Process Accounts](#3-process-accounts)
- [Save Updated Account Data](#4-save-updated-account-data)
- [Print the Updated Data](#5-print-the-updated-data)
- [Source Code Review](#6-source-code-review)

## Description

For this assignment 3 we are going to create a bank automated teller machine simulator

### ATM Simulator.py

- To simulate a transaction of PIXELL RIVER FINANCIAL on the system.
- To easily manage bank account transactions.
- To Create a Deposit, Withdraw and Quit from the system.
- When pressing something invalid from the system should say "INVALID SELECTION"
- Updates the current balance every time when Deposit, Withdraw etc.
- When pressed quit the system should output and tell the user the program will exit.

### Interest Update.py

- To apply interest based on balance accounts
- To apply interest based on how much they hold $$$ if so increase the interest
- To grow wealth overtime based on balance

## Assignment Instructions

## ATM Simulator Requirements

ATM Simulator User Story
As a Pixell River Financial customer,

I want to use a simulated ATM for deposit and withdraw transactions,

So that I can easily manage my bank account transactions.

## [1] Update the README File

Update the README.md file to include a description of the automatic_teller_machine.py program based on the User Story above. This information will be added to the end of the file.

Use the following format:

```cs
## [Program Name]

[Describe the intention of the program based on the User Story.]
```

## [2] Define User Interface

Edit the automatic_teller_machine.py module created earlier to define the user interface.

### Menu Options

Define a collection to store the following values:

"D"
"W"
"Q"
These values represent the menu options of Deposit, Withdraw and Quit.

### Customer Initial Balance

Since the program is a simulator, the customer's initial bank balance will be a randomly generated value between -1,000 and 10,000. 
Setting the customer's initial bank balance must only happen once per program execution.

### Selection Menu

The ATM Simulator starts by displaying the selection menu. 
The ATM display has a maximum width of 40 characters.

Format:

```cs
****************************************
         PIXELL RIVER FINANCIAL
             ATM Simulator

   Your current balance is: {balance}

               Deposit: D
              Withdraw: W
                Quit: Q
****************************************

Example:

****************************************
         PIXELL RIVER FINANCIAL
             ATM Simulator

   Your current balance is: $9,740.00   

               Deposit: D
              Withdraw: W
                Quit: Q
****************************************
```

```cs
 Important!
The program output will not include "{balance}". This is only part of the format requirement to show you where the balance value will be included.
```

The selection menu must have the following characteristics:

Lines 2 - 7: Text is centered to the ATM display.
Line 4: The account balance is formatted using currency formatting ($###,##0.00).

## [3] Processes Transactions

### Menu Selection Prompt

After the selection menu is displayed to the customer, the customer is prompted to enter a menu selection.

```cs
Enter your selection: {selection}

Note!
The output will not include "{selection}". 
It is only part of the format to show you where a menu selection will be entered.
```

The prompt will be printed on the very next line following the selection menu. Do not include any blank lines after the menu and before the selection prompt:

```cs
                Quit: Q
****************************************
Enter your selection: {selection}
```

### Menu Selection Validation

After the user enters their selection, the selection input is validated. The selection input is considered valid when it matches one of the defined Menu Options.
Also consider that the selection is case-insensitive, meaning that both a lowercase and uppercase selections are considered valid. For example 'q' and 'Q' are both valid entries.

If an invalid selection is made, the following is printed to the ATM display:

```cs

****************************************
           INVALID SELECTION
****************************************

Important!
The first line of the format requirement above is a blank line.

Example:

Enter your selection: t

****************************************
           INVALID SELECTION
****************************************
```

After displaying the invalid selection message, the program will pause and the display is cleared
before displaying the Selection Menu
again.

### Deposit or Withdraw Selection

When the user chooses to make a Deposit or Withdraw from their bank account, the user will be prompted for a transaction amount as follows:

```cs
Enter the transaction amount: {amount}
```

```cs
Note!
The output will not include "{amount}". It is only part of the format requirement to show you where the amount will be entered.
```

```cs
IMPORTANT!
You will assume that the user will only enter a positive numeric value. DO NOT valid the transaction amount input.
```

The transaction prompt will happen on the very next line after the menu selection prompt.

```cs
Example:
Enter your selection: w
Enter the transaction amount: {amount}
```

### Processing a Transaction

- Deposit
When the customer chooses to make a Deposit, the transaction amount entered by the customer will be added to their current bank balance. After the account balance is updated, the Account Balance Message
is printed to the ATM display.

- Withdrawal
When the customer chooses to make a Withdrawal, the transaction can only be successful if the customer withdraws an amount less than or equal to their current bank balance.
If the customer attempts to withdraw an amount greater than they currently have in their bank account balance, an Insufficient Funds Message
is printed to the ATM display.

```cs
Important!
The customer's bank balance is not updated when a withdraw transaction is not successful.
```

When the customer enters a valid transaction amount to be withdrawn, the transaction amount is deducted from the customer's bank balance. After the account balance is updated, the Account Balance Message
is printed to the ATM display.

### Account Balance Message

```cs
When the account balance message is displayed, the output is formatted as:
***************************************
   Your current balance is: {balance}
***************************************
```

### Insufficient Funds Message

```cs
When the insufficient funds message is displayed, the output is formatted as:
****************************************
           INSUFFICIENT FUNDS
****************************************
```

The format requirement above includes a blank line on line 1 and the text on line 3 is centered.

### Process Transactions Testing

Test your work to ensure that all conditions are producing the correct results. Once you verified your program is producing the expected results, commit your changes.

```cs
 Save and Commit!
Save and commit your changes with a meaningful message.
```

## [4] Incorporate Multiple Transactions

Modify your code to allow the customer to process multiple transactions. The simulator will end when the customer chooses to Quit during Menu Selection
.

After each transaction is processed (see Processing a Transaction),
pause the program for three seconds and clear the ATM display of all text.
(See Pausing the Script and Clearing the Screen)

### Development Considerations

The use of break and/or continue must only be used to reduce code duplication or source code structure. Misuse of these statements can be a cause for deductions.

### Pausing the Script and Clearing the Screen

Use the code below to pause the script for three seconds, then clear the console screen:

```cs
# Pause the script for the specified number of seconds
sleep(3)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
```

The sleep() function is defined in a built-in Python module called time. os is also a built-in Python module.

### Quit Menu Selection

When the customer chooses to Quit during Menu Selection,
no further output is printed and the program will end.

### Multiple Transaction Testing

Test your work to ensure your program is processing multiple transactions as specified in the requirements above.
Once you have verified the expected results, commit your changes.

```cs
Save and Commit!
Save and commit your changes with a meaningful message.
```

## [5] Source Code Review

Review your work to ensure it complies with the Course Development Standards opens in new window``.
Add comments at your discretion to support the maintenance of your program.
If you make any changes during the source code review, ensure you save and commit the changes to your repository.

## Interest Update Requirements

Interest Update User Story:

```cs
As the VP Client Services,

I want to apply interest to multiple customers' accounts based on their current balance,

So that I can help our customers grow their wealth over time.
```

## Update the README File

Open the README.md file created earlier.

Update the file to include a description of the interest_update.py program based on the User Story above.

Use the following format:

```cs
## [Program Name]

[Describe the intention of the program based on the User Story.]
```

```cs
Save and Commit!
Save and commit your changes with a meaningful message.
```

## [2] Print Customer Balances

Open the interest_update.py file created during the project setup.

Define an empty Dictionary that will be used to store the contents of the file containing the customers' account balances.

Open the given input file named account_balances.txt in read mode using a context manager (with clause).

The input file is pipe-delimited (|), with an account number, a pipe and the account balance on each line as shown below (only the first 4 records are shown):

```cs
C-0001|1024.12
C-0002|49025.19
C-0003|5.29
C-0004|-599.33
etc...
```

Process the data in the file by splitting each row based on the pipe delimited. Add the contents of the input file to the Dictionary defined above by assigning the Account Number as the key and the Account Balance as the value.

Use the Pretty Print opens in new window``module to display the contents of the Dictionary to the console.

```cs
Save and Commit!
Save and commit your changes with a meaningful message.
```

## [3] Process Accounts

Iterate through the Dictionary of bank accounts and calculate the interest earned for each account.
    - Positive balances less than $1000.00 will receive interest at a rate of 1.0%
    - Positive balances less than $5000.00 but $1000.00 or greater will receive interest at a rate of 2.5%
    - Positive balances $5000.00 or greater will receive interest at a rate of 5.0%
    - Negative balances will be charged interest at a rate of 10.0%

The formula for calculating monthly interest is as follows:

```cs
monthly interest = balance * rate
                -------------------
                        12
```

Update the balance of each bank account in the Dictionary to reflect the interest earned or charged. Do not perform any rounding operations on the data.

Below are examples of balance calculations (to 6 decimal places) before and after interest has been applied:

```cs
Opening Balance	Closing Balance	Earned/Charged
5000.00	5020.833333	5% interest earned
2000.00	2004.166667	2.5% interest earned
850.00	850.708333	1% interest earned
-595.00	-599.958333	10% interest charged
0.00	0.000000	no interest earned or charged
```

Use the Pretty Print opens in new window``module to display the contents of the Dictionary to the console.

```cs
Warning!
Use a calculator to confirm the expected results.

Save and Commit!
Save and commit your changes with a meaningful message.
```

## [4] Save Updated Account Data

The updated account information will be saved to a .csv (Comma-delimited file format). This file will be created within your script if it does not already exist. If the file already exists, the existing data within the file will be overwritten.

Name the file in the following format: updated_balances_FL.csv where FL represents the initials of your first and last name. For example, for "Jo-Anne Sinclair", their initials are "JS", so the filename used would be updated_balances_JS.csv.

The following data will be written to the .csv file:

The first line of the file will contain heading data for "Account" and "Balance".
For each account in the Dictionary, print the account number and balance for the account to a line in the file. Each account will be printed to its own line in the file.
Sample:

```cs
Account,Balance
C-0001,1024.12
C-0002,49025.19
C-0003,5.29
C-0004,-599.33
```

```cs
Development Requirement!
DO NOT use DictWriter to complete this part of the program.
```

Verify the data has been successfully written to the file and that the file does not contain any blank rows.

```cs
Save and Commit!
Save and commit your changes with a meaningful message.
```

## [5] Print the Updated Data

Use the DictReader function opens in new window``of the built-in csv module to read the data stored in the .csv file created in the previous step.
Print the data from the .csv file to the console.

## [6] Source Code Review

Review your work to ensure it complies with the Course Development Standards opens in new window``.
Add comments at your discretion to support the maintenance of your program.
If you make any changes during the source code review, ensure you save and commit the changes to your repository.

[EOF]
