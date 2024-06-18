## Bank Account Management System

Name- Jashanpreet Singh
GitHub username - SinghJashan
edX username - jashan_2004
Video Demo - (https://youtu.be/bAYHc1gPzns)
city - Tarn-Taran, Punjab, India
date - **May-05-2024**


This is a simple console-based bank account management system implemented in Python.

## Features

The system provides the following features:

- **Open Account**: Open a new bank account.
- **Display Account**: View the details of an existing account.
- **Deposit Money**: Deposit money into an account.
- **Withdraw Money**: Withdraw money from an account.

## Usage

To use this system, run the script in your Python environment. You will be presented with a menu of options. Enter the corresponding command to perform an operation.

Here are the available commands:

- `open OR Open`: Open a new account.
- `display OR Display`: View the details of an account.
- `deposit OR Deposit`: Deposit money into an account.
- `withdraw OR Withdraw`: Withdraw money from an account.

## Classes

The system is implemented using a `Bank` class. Here are the methods of the `Bank` class:

- `__init__(self, ac_no=0, name="", balance=0)`: Initializes a new instance of the `Bank` class.
- `open(self, ac_no, name, balance)`: Opens a new account.
- `display(self)`: Displays the details of an account.
- `deposit(self, amount)`: Deposits money into an account.
- `withdraw(self, amount)`: Withdraws money from an account.

## Testing

Unit tests for the `Bank` class are included in the `test_bank.py` file. The tests cover the `open`, `deposit`, and `withdraw` methods of the `Bank` class.

To run the tests, use the following command:

```bash
python -m unittest test_bank.py
python test_project.py

```

## Note

- To run this project, firstly you need to run **pip install requirements.txt** in the terminal to install all required modules for this project.
