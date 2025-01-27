class Bank:
    bank_name ='SBI'
    def __init__(self, name, age, bal):
        self.user_name = name
        self.age = age
        self.user_balance = bal

    def get_info(self):
        print(f'''User name: {self.user_name} and
              user balance: {self.user_balance}
              for Bank: {self.bank_name}''')
        

b1 = Bank("Pooja", 23, 45567)
print(b1.bank_name) #SBI
print(Bank.bank_name) #SBI
b1.get_info()