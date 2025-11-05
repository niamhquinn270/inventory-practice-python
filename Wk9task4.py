class BankAccount:

    def __init__(self, name, accNo, openBal, overlimit):
        self.name = name
        self.accNo = accNo
        self.openBal = openBal
        self.overlimit = overlimit


    def __str__(self):
       return f"Account Name = {self.name}:"


