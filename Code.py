import json
import os
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepo:
    def __init__(self):
        self.users = []
        self.isloggedIn = False 
        self.currentUser = {}

        # load users from json file
        self.loadUser()

    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser =  User(username=user["username"], password=user["password"], email=user["email"]) 
                    self.users.append(newUser)
            print(self.users)

    def register(self, user : User):
        self.users.append(user)
        self.savetoFiles()
        print("User created.")

    def login(self, username, password):
        if self.isloggedIn:
            print("You already login")
        
        for user in self.users:
            if (user.username == username) and (user.password ==  password):  # Fix here
                self.isloggedIn = True
                self.currentUser = user
                print("Login successful")
            break

    def logout(self):
        self.isloggedIn = False
        self.currentUser = {}
        print("Exit successful ")

    def identity(self):
        if self.isloggedIn:
            print(f"username : {self.currentUser.username}")
        else :
            print("Login is not successful")
        

    def savetoFiles(self):

        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__)) 

        with open("users.json","w") as file:
            json.dump(list, file)

repository = UserRepo()
    
while True:
    print("Menu".center(50,"*"))
    choose = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n Choose one option : ")
    if choose == "5":
        break
    else:
        if choose == "1":
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")

            user = User(username = username, password = password, email = email)
            repository.register(user)
        elif choose == "2":
            username = input("Username : ")
            password = input("Password : ")

            repository.login(username, password)
           
        elif choose == "3":
            repository.logout()
            
        elif choose == "4":
            repository.identity()
        else :
            print("Wrong option!")
