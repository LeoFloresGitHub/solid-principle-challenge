# Here your solution
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

class DepositService:
    def __init__(self, account: BankAccount):
        self.account = account


    def execute(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.account.balance += amount

        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Deposited {amount} into {self.account.account_number}\n"
            )

        logging.info(f"Sending email notification: {amount} deposited into account {self.account.account_number}.")


class WithdrawService:
    def __init__(self, account: BankAccount):
        self.account = account

    def execute(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.account.balance:
            raise ValueError("Insufficient funds.")

        self.account.balance -= amount 

        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Withdrew {amount} from {self.account.account_number}\n"
            )

        logging.info(f"Sending email notification: {amount} withdrawn from account {self.account.account_number}.")


class StatementService:
    def __init__(self, account: BankAccount):
        self.account = account
        
    def execute(self):
        statement = f"Statement for Account: {self.account.account_number}\nBalance: {self.account.balance}\n"

        logging.info(statement)

        with open("statements.log", "a") as stmt_file:
            stmt_file.write(
                f"{datetime.datetime.now()}: Generated statement for {self.account.account_number}\n"
            )
        logging.info(f"Sending email with statement for account {self.account.account_number}...")


class BankSystem:
    def __init__(self, account_number: int):
        self.account = BankAccount(account_number)

    def deposit(self, amount):
        deposit_service = DepositService(self.account)
        deposit_service.execute(amount)

    def withdraw(self, amount): 
        withdraw_service = WithdrawService(self.account)
        withdraw_service.execute(amount)
        

    def generate_statement(self): 
        statement_service = StatementService(self.account)
        statement_service.execute()


bank_system = BankSystem(1954484654) 
bank_system.deposit(109)
bank_system.withdraw(22)
bank_system.generate_statement()