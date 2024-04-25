from datetime import datetime
class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
class Bank:
    def __init__(self, act_NB, act_Name, act_balance, IDnumber, accounttype, creation_date):
        self.act_NB = act_NB
        self.act_balance = act_balance
        self.act_Name = act_Name
        self.IDnumber = IDnumber
        self.accounttype = accounttype
        self.creation_date = creation_date

def create_account():
    global next_act_NB, accounts
    accounttype = input("\n\n🔷Enter account type "+Color.YELLOW+"(saving/mobile): "+Color.END)
    IDnumber = input("🔷Enter ID number: ")
    act_Name = input("🔷Enter account holder Name: ")
    act_balance = float(input("🔷Enter initial balance (minimum amount = RS:500) "+Color.YELLOW +"RS:"+Color.END))
    if act_balance < 500:
        print(Color.RED+"Initial balance must be at least 500.🔔"+Color.END)
        return
    act_NB = next_act_NB
    next_act_NB += 1
    creation_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    accounts[act_NB] = Bank(act_NB, act_Name, act_balance, IDnumber, accounttype, creation_date)
    print("🔴Account created successfully.")
    print(Color.BOLD+"🔴Your account number is: "+Color.END +Color.BOLD+Color.RED+f"{act_NB}" +Color.END)

def view_account_detail():
    accountNB = int(input("\n\n🔷Enter account number: "))
    if accountNB not in accounts:
        print(Color.RED+"️❌Account does not exist.🔔"+Color.END)
        return
    account = accounts[accountNB]
    print("🔴Account Number :",  Color.BLUE + str(account.act_NB) + Color.END)
    print("🔴Account Holder Name:",Color.BLUE + str( account.act_Name) + Color.END)
    print("🔴ID Number:", Color.BLUE + str(account.IDnumber) + Color.END)
    print("🔴Account Type:", Color.BLUE + str(account.accounttype) + Color.END)
    print("🔴Balance " + Color.YELLOW + "RS:" "{:.2f}".format(account.act_balance) + Color.END)
    print("🔴Creation Date:", Color.BLUE + account.creation_date + Color.END)

def check_balance():
    accountNB = int(input("\n\n🔷Enter account number: "))
    if accountNB not in accounts:
        print(Color.RED+"️❌Account does not exist.🔔"+Color.END)
        return
    account = accounts[accountNB]
    print("🔴Balance " + Color.YELLOW + "RS:""{:.2f}".format(account.act_balance) + Color.END)
    print("🔴Name:", account.act_Name)

def deposit():
    accountNB = int(input("\n\n🔷Enter account number: "))
    if accountNB not in accounts:
        print(Color.RED+"❌Account does not exist.🔔"+Color.END)
        return
    amount = float(input("🔷Enter the amount to deposit: " +Color.YELLOW +"RS:"+Color.END))
    if amount <= 0:
        print("🔴Amount to deposit must be greater than 0.")
        return
    account = accounts[accountNB]
    account.act_balance += amount
    print("🔴Deposit successful.")
    print("🔴New balance : {:.2f}"+Color.YELLOW +"RS".format(account.act_balance)+Color.END)

def withdraw():
    accountNB = int(input("\n\n🔷Enter account number: "))
    if accountNB not in accounts:
        print(Color.RED+"❌Account does not exist.🔔"+Color.END)
        return
    amount = float(input("🔷Enter the amount to withdraw: "))
    account = accounts[accountNB]
    if amount <= 0:
        print("🔴Amount to withdraw must be greater than 0.🔔")
        return
    if account.act_balance < amount:
        print(Color.RED+"❌Insufficient balance.🔔"+Color.END)
        return
    account.act_balance -= amount
    print("🔴Withdrawal successful.")
    print("🔴New balance RS: {:.2f}".format(account.act_balance))
def transfer():
    from_account = int(input("\n\n🔷Enter your account number: "))
    to_account = int(input("🔷Enter recipient's account number: "))
    if from_account not in accounts or to_account not in accounts:
        print(Color.RED+"❌One or both accounts do not exist.🔔"+Color.END)
        return
    amount = float(input("🔷Enter the amount to transfer :"+Color.YELLOW +"RS:"+Color.END))
    if amount <= 0:
        print("🔴Amount to transfer must be greater than 0.🔔")
        return
    if accounts[from_account].act_balance < amount:
        print("🔴Insufficient balance for transfer.🔔")
        return
    accounts[from_account].act_balance -= amount
    accounts[to_account].act_balance += amount
    print("🔴Transfer successful.")
    print("🔴New balance your RS: {:.2f}".format(accounts[from_account].act_balance))
    print("🔴New balance for recipient RS: {:.2f}".format(accounts[to_account].act_balance))

def About():
    print(Color.GREEN +"\n\n**************************************************"+Color.END)

    print(Color.GREEN + "*" + Color.END + Color.BLUE + "                   About US                     " + Color.END + Color.GREEN + "*" + Color.END)
    print(Color.GREEN + "*" + Color.END + Color.YELLOW + "        MINI PROJECT scenario [EEI3372]         " + Color.END + Color.GREEN + "*" + Color.END)
    print(Color.GREEN + "*" + Color.END + Color.YELLOW + "  This is simple bank account management system " + Color.END + Color.GREEN + "*" + Color.END)
    print(Color.GREEN + "*" + Color.END + Color.YELLOW + "     creat by"+Color.RED+ " 😃W.A.H.DENUWAN (S23010632)       " + Color.END + Color.GREEN + "*" + Color.END)
    print(Color.GREEN+"**************************************************"+Color.END)

accounts = {}
next_act_NB = 2002

def main():
    while True:
        print(Color.GREEN+"\n*************************************"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.YELLOW+"💰----------🙏WELLCOME🙏---------💰"+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.YELLOW+"--------------NCN_BANK🇱🇰------------"+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*************************************"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.BLUE+" 1. Create Account            👈   "+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.BLUE+" 2. Deposit                   👈   "+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.BLUE+" 3. Withdraw money            👈   "+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.BLUE+" 4. Check Balance             👈   "+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.BLUE+" 5. Transfer money            👈   "+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.BLUE+" 6. View Account Detail       👈   "+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*"+Color.END+Color.BLUE+" 7. About                     👈   " + Color.END + Color.GREEN + "*" + Color.END)
        print(Color.GREEN+"*"+Color.END+Color.BLUE+" 8. Exit                      👈   "+Color.END+Color.GREEN+"*"+Color.END)
        print(Color.GREEN+"*************************************"+Color.END)
        choice = input(" 😃:::"+Color.RED+"Enter your choice"+Color.END+":  \t")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transfer()
        elif choice == "6":
            view_account_detail()
        elif choice == "7":
            About()
        elif choice == "8":
            print(Color.RED +"Exiting......"+Color.END)
            break
        else:
            print(Color.RED + "️Invalid. Please try again.🔔" + Color.END)

if __name__ == "__main__":
    main()





