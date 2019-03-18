import datetime


def log_error(error_msg):
    with open("error.log", "a") as error_file:
        error_file.write("{}\t{}\n".format(datetime.datetime.now(), error_msg))


class BankAccount(object):
    """ """
    WITHDRAW_PROMPT = "Please Enter a Withdraw Amount:"
    DEPOSIT_PROMPT = "Please Enter a Deposit Amount:"

    def __init__(self, bank_balance=0):
        self.bank_balance = bank_balance

    def getAmountFromConsole(self, prompt):
        error = True
        while error:
            amount = input(prompt)
            try:
                amount = int(amount)
                error = False
            except ValueError as e:
                print("Invalid Input")
                log_error(str(e))
        return amount

    def deposit(self):
        amount = self.getAmountFromConsole(self.DEPOSIT_PROMPT)
        self.bank_balance = self.bank_balance + amount
        self.balance()

    def withdraw(self):
        amount = self.getAmountFromConsole(self.WITHDRAW_PROMPT)
        self.bank_balance = self.bank_balance - amount
        self.balance()

    def balance(self):
        print("Current Balance: {}".format(self.bank_balance))


bank_account = BankAccount()
bank_account.deposit()
bank_account.deposit()
bank_account.withdraw()
bank_account.withdraw()