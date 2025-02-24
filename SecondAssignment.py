import json
class MiniBank:
    mainUserInfo={}

    def __init__(self):

        self.loadData()

    def loadData(self):
        try:
            with open('PROJECT.txt', 'r')as file:
                self.mainUserInfo=json.load(file)
        except FileNotFoundError:
            print("File not found")

    def saveData(self):
        with open('PROJECT.txt', 'w')as file:
            json.dump(self.mainUserInfo,file)
            print("Data saved successfully>>")

    def firstOption(self):
        option=int(input("\nPress 1 to LOGIN:__\n Press 2 to REGISTOR:__"))
        if option==1:
            self.login()
        elif option==2:
            self.register()

    def login(self):
        username=str(input("Enter username to login::"))
        password=int(input("Enter password to login::"))
        for user_id,user in self.mainUserInfo.items():
            if user["r_username"]==username and user["r_passcode"]==password:
                print("Login successful!!")
                self.menu((user_id))
                return
        print("Invalid login__")

    def register(self):
        username = input("Enter username: ")
        amount = int(input("Enter initial deposit amount:__ "))
        passcode = int(input("Enter passcode:__ "))
        passcode2 = int(input("Pls enter again passcode to confirm:__"))

        if passcode==passcode2:
            id=self.CheckinguserCount()
            userInfoForm={id: {"r_username": username, "r_passcode": passcode, "amount": amount}}
            self.mainUserInfo.update(userInfoForm)
            print("___Success registor__\n\n")
            print(self.mainUserInfo)
            self.saveData()
        else:
            print("Password not match,Try again__")

    def CheckinguserCount(self):
        count=len(self.mainUserInfo)
        return count+1

    def menu(self, user_id):
        while True:
            print("1. Transfer>>\n2. Withdraw>>\n3. Update>>\n4. Log out___")
            choice = int(input("Choose an option:__ "))
            if choice == 1:
                self.transfer(user_id)
            elif choice == 2:
                self.withdraw(user_id)
            elif choice == 3:
                self.update(user_id)
            elif choice == 4:
                print("Logging out...")
                break
            else:
                print("<<Try again.>>")

    def transfer(self, user_id):
        to_username = input("Enter recipient username:__ ")
        for id, user in self.mainUserInfo.items():
            if user["r_username"] == to_username:
                amount = int(input("Enter amount to transfer:__ "))
                if self.mainUserInfo[user_id]["amount"] >= amount:
                    self.mainUserInfo[user_id]["amount"] -= amount
                    self.mainUserInfo[id]["amount"] += amount
                    print(f"Transferred {amount} to {to_username}, Current balance: {self.mainUserInfo[user_id]['amount']} ")
                    self.saveData()  # Save the updated data to the file
                    return
                else:
                    print("Insufficient funds.")
                    return
        print("Recipient not found.")

    def withdraw(self, user_id):
        amount = int(input("Enter amount to withdraw:__ "))
        w_pwd = int(input("PLS,Enter your password to withdraw___"))

        if self.mainUserInfo[user_id]["r_passcode"] == w_pwd:
            if self.mainUserInfo[user_id]["amount"] >= amount:
                self.mainUserInfo[user_id]["amount"] -= amount
                print(f"Withdrew {amount}. Current balance: {self.mainUserInfo[user_id]['amount']}")
                self.saveData()
            else:
                print("Insufficient funds!")
        else:
            print("Invalid password. Try again.")

    def update(self, user_id):
        print("1. Update Username__\n2. Update Password__\n3. Update Balance__")
        choice = int(input("Select option to update:__ "))
        if choice == 1:
            new_username = input("Enter new username:__")
            self.mainUserInfo[user_id]["r_username"] = new_username
            print("Username updated: ", new_username)

        elif choice == 2:
            new_passcode = int(input("Enter new password:__ "))
            self.mainUserInfo[user_id]["r_passcode"] = new_passcode
            print("Password updated.")
        elif choice == 3:
            new_balance = int(input("Enter new balance:__ "))
            self.mainUserInfo[user_id]["amount"] += new_balance
            print(f"Balance updated. New balance: {self.mainUserInfo[user_id]['amount']}")
        else:
            print("Invalid choice.")

        self.saveData()

if __name__=="__main__":
    miniBank=MiniBank()
    while True:
       miniBank.firstOption()