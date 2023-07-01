import datetime


class Account:
    AUO_TD = 10000000000
    def __init__(self,ower, start,end,balance,bank,
                 balance_moth,fee,state):
        self.number_bank = f'VCB{Account.AUO_TD}'
        self.ower = ower
        self.start = start
        self.end = end
        self.balance = balance
        self.bank = bank
        self.balance_moth = balance_moth
        self.fee = fee
        self.state = state
        Account.AUO_TD += 1
    def chech_balance(self):
        if self.state == 1:
            print(f"--SO DU CUA TAI KHOAN LA: {self.balance}")
    def chuyentien(self,other,money):
        if self.state == 1 and other.state == 1:
            if self.balance - money > 70000 and money > 0:
                self.balance -= money
                other.balance += money
                print("COMPLETE")
                return 1
            else:
                print("FAIL : BALANCE NOT ENOUGH")
                return 0
        else:
            print("YOUR ACCOUNT IS LOCKED")
            return 0
    def naptien(self,money):
        if self.state  > 0 :
            if money > 0:
                self.balance += money
                print("COMPLETE")
                return 1
        else:
            print("YOUR ACCOUNT IS LOCKED")
            return 0

    def ruttien(self,money):
        if self.state == 1:
            if self.balance - money > 70000 and money > 0:
                self.balance -= money
                print("COMPLETE")
                return 1
            else:
                print("FAIL : BALANCE NOT ENOUGH")
                return 0
        else:
            print("YOUR ACCOUNT IS LOCKED")
            return 0
    def saving(self,money):
        if self.state == 1:
            if money > 0:
                self.balance -= money
                print("SAVING COMPLETE")
                return 1
            else:
                print("MONEY IS INVALID")
        else:
            print("YOUR ACCOUNT IS LOCKED")
            return 0
    def pay_bill(self,money):
        if self.state == 1:
            if self.balance - money > 70000 and money > 0:
                self.balance -= money
                print("PAY BILL COMPLETE")
                return 1
            else:
                print("FAIL : BALANCE NOT ENOUGH")
                return 0
        else:
            print("YOUR ACCOUNT IS LOCKED")
            return 0
    def __str__(self):
        return f'{self.ower} {self.balance} {self.number_bank} {self.bank} state: {self.state}'
class DomesticAccount(Account):

    def __init__(self, ower, start, end, balance, bank,
                 balance_moth, fee, state,limit):
        super().__init__(ower,start,end,balance,
                         bank,balance_moth,fee,state)
        self.fee_in = 1100
        self.fee_out = 3300
        self.limit = limit

    def ruttien(self,money,bank = True):
        if money < self.limit:
            if super().ruttien(money) > 0 :
                if bank is True:
                    self.balance -= self.fee_in
                else:
                    self.balance -= self.fee_out
                return 1
        else:
            print("SO TIEN VUOT QUA GIOI HAN")
            return 0

    def chuyentien(self,other,money):
        if self.limit > money:
            super().chuyentien(other,money)
        else:
            print("MONEY IS LIMIT")

    def __str__(self):
        return f'DomesticAccount: {super().__str__()}'
class VisaAccount(Account):
    AUO_TD = 10000000
    def __init__(self, ower, start, end, balance, bank,
                 balance_moth, fee, state, limit):
        super().__init__(ower, start, end, balance,
                         bank, balance_moth, fee, state)
        self.limit = limit
        self.id_internation = VisaAccount.AUO_TD
        VisaAccount.AUO_TD += 1
        self.fee_in = 1100
        self.fee_out = 9900
        self.fee_pay_bill = 23500

    def ruttien(self,money,bank = True):
        if super().ruttien(money) > 0 and money < self.limit:
            if bank is True:
                self.balance -= self.fee_in
            else:
                self.balance -= self.fee_out
            return 1
        else:
            return 0
    def __str__(self):
        return f'VisaAccount {super().__str__()}'
class ATM:
    AUTO_ID = 10000000
    def __init__(self,bank,address,state):
        self.id = ATM.AUTO_ID
        self.bank = bank
        self.address = address
        self.state = state
class Transaction:
    AUTO_ID = 10000000
    def __init__(self,num_bank,name,fee,result):
        self.id = Transaction.AUTO_ID
        self.num_bank = num_bank
        self.name = name
        self.fee = fee
        self.result = result
        self.time = datetime.datetime.now()
        Transaction.AUTO_ID += 1

    def info(self):
        ate_str = f'{self.time.day:02}/{self.time.month:02}/' \
                  f'{self.time.year:4} {self.time.hour:02}:' \
                  f'{self.time.minute:02}:{self.time.second:02}'
        return f'MA_GIAO DICH: {self.id} {self.num_bank} ' \
               f'Kieu giao dich: {self.name} FEE {self.fee} ' \
               f'{self.result} {ate_str}'

    def __str__(self):
        ate_str = f'{self.time.day:02}/{self.time.month:02}/' \
                  f'{self.time.year:4} {self.time.hour:02}:' \
                  f'{self.time.minute:02}:{self.time.second:02}'
        return f'MA_GIAO DICH: {self.id} {self.num_bank} '\
               f'Kieu giao dich: {self.name} FEE {self.fee} '\
                f'{self.result} {ate_str}'

def creat_account():
    account = []
    with open('domcard.dat','r+') as inp:
        while True:
            name = inp.readline().strip()
            if name == '':
                break
            start = inp.readline().strip()
            end = inp.readline().strip()
            balance = int(inp.readline().strip())
            bank = inp.readline().strip()
            balance_month = inp.readline().strip()
            fee = inp.readline().strip()
            state = int(inp.readline().strip())
            limit = int(inp.readline().strip())
            account.append(DomesticAccount(name,start,end,balance,bank,balance_month,fee,state,limit))
    return account
def print_arr(arr):
    for i in arr:
        print(i)
def find_account(acc,id):
    for i in acc:
        if i.number_bank == id:
            return i
    return None
def nap_tien(acc,out):
    print("Nhap so tk:")
    id  = input()
    acc = find_account(acc,id)
    if acc is not None:
        money = int(input('Nhap so tien muon nap '))
        re = acc.naptien(money)
        if re > 0:
             out.write(Transaction(acc.number_bank,"NAP TIEN",0,"COMPLETE").__str__() + '\n')

        else:
             out.write(Transaction(acc.number_bank, "NAP TIEN", 0, "FAIL").__str__() + '\n')
             out.write('\n')

def rut_tien_same(acc,out):
    print("Nhap so tk:")
    id = input()
    acc = find_account(acc, id)
    if acc is not None:
        money = int(input('Nhap so tien muon rut: '))
        re = acc.ruttien(money)
        if re > 0:
            out.write(Transaction(acc.number_bank, "RUT TIEN", acc.fee_in, "COMPLETE").__str__() + '\n')
            out.write('\n')
        else:
            out.write(Transaction(acc.number_bank, "RUT TIEN", acc.fee_in, "FAIL").__str__() + '\n')
            out.write('\n')
def pay_bill_in(acc,out):
    print("Nhap so tk:")
    id = input()
    acc = find_account(acc, id)
    if acc is not None and isinstance(acc,DomesticAccount):
        money = int(input('Nhap so tien bill: '))
        re = acc.pay_bill(money)
        if re > 0:
             out.write(Transaction(acc.number_bank, "THANH TOAN HOA DON TRONG NUOC ", 0, "COMPLETE").__str__() + '\n')
             out.write('\n')
        else:
            out.write(Transaction(acc.number_bank, "THANH TOAN HOA DON TRONG NUOC", 0, "FAIL").__str__() + '\n')
            out.write('\n')

accounts = creat_account()

menu =0
while menu != 10:
    menu = int(input("NHAP MENU: "))
    if menu == 1:
        print("DANH SACH CÁC TÀI KHOẢN LA:")
        print_arr(accounts)
    if menu == 2:
        with open('tran.dat','a+') as out:
            nap_tien(accounts,out)
    if menu == 3:
        with open('tran.dat', 'a+') as out:
             rut_tien_same(accounts,out)
    if menu == 4:
        with open('tran.dat', 'a+') as out:
            pay_bill_in(accounts,out)








