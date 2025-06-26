import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"an exception occured:{err}")
    @staticmethod
    def __update(cls):
        with open(cls.database,'w')as fs:
            fs.write(json.dumps(cls.data,indent=4))
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id= alpha + num +spchar
        random.shuffle(id)
        return "".join(id)




    def createAccount(self):
        info={
            "name":input("Enter your name:-"),
            "age":int(input("Enter your age:-")),
            "email":input("Enter your email:-"),
            "pin":int(input("Enter your pin:-")),
            "accountNo":Bank.__accountgenerate(),
            "balance":0
        }

        if info['age'] < 18 or len(str(info["pin"]))!=4:
            print("Sorry you cannot create a bank account")
        else: 
            print("Pls note down your account number")
            for i in info:
                print(f"{i} : {info[i]}")
                
        Bank.data.append(info)
        Bank.__update(Bank)
        print("Account has been created successfully")
    def depositmoney(self):
        accnum =input("pls tell your Account no.-:")
        pin=(input("Pls tell your Pin:-"))
        userdata=[i for i in Bank.data if i['accountNo']==accnum and str(i['pin'])==pin]
        if not  userdata:
           print("Sorry No data Found")
           return 
        user=userdata[0]
        
        try:
                  amount=int(input("How much you want to deposit:-"))
        except ValueError:
                print("❌ Invalid amount! Please enter a number.")
                return

        if amount >1000:
                print("Sorry the amount is too much you can deposit amount below 10000 ")
                return
         
                
        user['balance'] += amount
        Bank.__update(Bank)
        print(f"Amount deposited successfully. New balance: ₹{user['balance']}")
    def withdrawmoney(self):
        accnum =input("pls tell your Account no.-:")
        pin=(input("Pls tell your Pin:-"))
        userdata=[i for i in Bank.data if i['accountNo']==accnum and str(i['pin'])==pin]
        if not  userdata:
           print("Sorry No data Found")
           return 
        user=userdata[0]
        
        try:
             amount = int(input("How much you want to withdraw:-"))
        except ValueError:
             print("❌ Invalid amount! Please enter a number.")
             return
        if userdata[0]['balance']<amount:
             print("Sorry you don't have that much money")
        user['balance'] -= amount
        Bank.__update(Bank)
        print(f"Amount withdrawn  successfully")
    def showdetails(self):
        accnum = input("pls tell your Account no.-:")
        pin = input("Pls tell your Pin:-")
        userdata = [i for i in Bank.data if i['accountNo'] == accnum and str(i['pin']) == pin]
        if not userdata:
            print("❌ No account found with that number and pin.")
            return
        print("\n✅ Your account details are:\n")
        user = userdata[0]
        for key, value in user.items():
            print(f"{key}: {value}")
    def updatedetails(self):
        accnum = input("Please tell your Account no.: ").strip()
        pin = input("Please tell your Pin: ").strip()

        
        userdata = [i for i in Bank.data if i['accountNo'] == accnum and str(i['pin']) == pin]

        if not userdata:
            print("❌ No such user found!")
            return

        print("\nYou cannot change age, account number, or balance.")
        print("Leave any field blank to keep the existing value.")

       
        user = userdata[0]

        new_name = input("Enter new name (or press Enter to skip): ").strip()
        new_email = input("Enter new email (or press Enter to skip): ").strip()
        new_pin_input = input("Enter new 4-digit pin (or press Enter to skip): ").strip()
        newdata = {
            "name": new_name if new_name else user["name"],
            "email": new_email if new_email else user["email"],
            "pin": int(new_pin_input) if new_pin_input.isdigit() and len(new_pin_input) == 4 else user["pin"],
            "age": user["age"],
            "accountNo": user["accountNo"],
            "balance": user["balance"]
        }

        index = Bank.data.index(user)
        Bank.data[index] = newdata
        Bank.__update(Bank)

        print("✅ Your details have been successfully updated!")
    def deleteaccount(self):
        accnum = input("Please tell your Account no.: ").strip()
        pin = input("Please tell your Pin: ").strip()

        
        userdata = [i for i in Bank.data if i['accountNo'] == accnum and str(i['pin']) == pin]
        if not userdata:
         print("❌ No account found with that number and PIN.")
         return

        user = userdata[0]
        confirm = input(f"⚠️ Are you sure you want to delete the account '{accnum}'? Type YES to confirm: ").strip().upper()
        if confirm == "YES":
          Bank.data.remove(user)
          Bank.__update(Bank)
          print("✅ Your account has been deleted successfully.")
        else:
           print("❌ Account deletion cancelled.")

user=Bank()


print("Press 1 for creating your account")
print("Press 2 for depositing  money in bank")
print("Press 3 for withdrawing money from bank")
print("Press 4 for  details")
print("Press 5 for updating details")
print("Press 6 for deleting your account")

check =int(input("Tell your response:- "))
 
if check==1:
    user.createAccount()
if check==2:
    user.depositmoney()
if check==3:
    user.withdrawmoney()
if check==4:
    user.showdetails()
if check==5:
    user.updatedetails()
if check==6:
    user.deleteaccount()

