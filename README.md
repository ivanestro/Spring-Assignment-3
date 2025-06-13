# Assignment 3

## Contents

- [Description](#description)
- [Author](#author)
- [Assignment Instructions](#assignment-instructions)

## Description

For this assignment 3 we are going to create a bank automated teller machine simulator

- To simulate a transaction of PIXELL RIVER FINANCIAL on the system.
- To create a Deposit, Withdraw and Quit from the system.
- When pressing something invalid from the system should say "INVALID SELECTION"
- Updates the current balance every time when Deposit, Withdraw etc.
- To easily manage bank account transactions.
- When pressed quit the system should output and tell the user the program will exit.

## Author

Ivan Estropigan

## Assignment Instructions

1. Update the README File


Update the README.md file to include a description of the automatic_teller_machine.py program based on the User Story above. This information will be added to the end of the file.

Use the following format:

```cs
## [Program Name]

[Describe the intention of the program based on the User Story.]
```

2. Define User Interface

Edit the automatic_teller_machine.py module created earlier to define the user interface.

```cs
Menu Options
Define a collection to store the following values:

"D"
"W"
"Q"
These values represent the menu options of Deposit, Withdraw and Quit.

Customer Initial Balance
Since the program is a simulator, the customer's initial bank balance will be a randomly generated value between -1,000 and 10,000. 
Setting the customer's initial bank balance must only happen once per program execution.

Selection Menu
The ATM Simulator starts by displaying the selection menu. 
The ATM display has a maximum width of 40 characters.

Format:

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

The selection menu must have the following characteristics:

Lines 2 - 7: Text is centered to the ATM display.
Line 4: The account balance is formatted using currency formatting ($###,##0.00).
```

3. Processes Transactions

Menu Selection Prompt
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

Menu Selection Validation
After the user enters their selection, the selection input is validated. The selection input is considered valid when it matches one of the defined Menu Options
. Also consider that the selection is case-insensitive, meaning that both a lowercase and uppercase selections are considered valid. For example 'q' and 'Q' are both valid entries.

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

[EOF]
