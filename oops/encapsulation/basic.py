class account:
    def __init__(self,ac_no,balance):
        self.ac_no = ac_no
        self.__balance = balance
    def details(self):
        print(self.__balance)
    
u1 = account(1234,2000)
u1.b