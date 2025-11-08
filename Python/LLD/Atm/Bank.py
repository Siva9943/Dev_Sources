
class Bank:
    def __init__(self):
        self.accounts = {
            '9943': {'pin': 1234, 'balance': 800000},
            '9056': {'pin': 1232, 'balance': 303330},
            '6732': {'pin': 7357, 'balance': 100},
        }

    def create_account(self, account_id, initial_balance=0):
        if account_id in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[account_id] = {'pin': None, 'balance': initial_balance}

    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.accounts[account_id] += amount

    def withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.accounts[account_id] < amount:
            raise ValueError("Insufficient funds.")
        self.accounts[account_id] -= amount

    def get_balance(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist.")
        return self.accounts[account_id]
# user account details
class User_Details(Bank):
    def __init__(self, input_card_number, input_pin):
        self.input_card_number = input_card_number
        self.input_pin = input_pin

    def validate(self, input_card_number, input_pin):
        super().__init__()
        if input_card_number in self.accounts:
            if self.accounts[input_card_number]['pin'] == input_pin:
                return True
        return False
    def get_user_balance(self, input_card_number):
        super().__init__()
        if input_card_number in self.accounts:
            return self.accounts[input_card_number]['balance']
        else:
            raise ValueError("Account does not exist.")
