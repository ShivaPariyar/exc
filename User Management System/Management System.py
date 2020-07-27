# we are creating User Management System
"""
We use 3 Modules:
1. User Module
2. Role Module: role for the user and the manager
3. Permissions Module : right for the Project Manager. Access to all files
"""
"""
For User Module We use MVC Framework:
M = Model: stores data and logic (cook)
V = View: presentation of data from the Model to the user. (frontend) (customer)
C = Controller: handles the interaction of the user and pass the data to the model. (Waiter)
"""

# M = Model: stores data and logic (cook)
class User_Model:
    user_list = []
    data = dict()

    def __init__(self, user_id):
        self.user_id = user_id
        self.user_list.append(self.user_id)

    def create(self,first_name, last_name, user_name, email_id, password ):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email_id = email_id
        self.password = password
        self.user_list.append(self.first_name)
        self.user_list.append(self.last_name)
        self.user_list.append(self.user_name)
        self.user_list.append(self.email_id)
        self.user_list.append(self.password)



    def database_fake():
        User_Model.data["user ID"] = User_Model.user_list[0]
        User_Model.data["first name"] = User_Model.user_list[1]
        User_Model.data["last name"] = User_Model.user_list[2]
        User_Model.data["user name"] = User_Model.user_list[3]
        User_Model.data["password"] = User_Model.user_list[4]

#add user query
#	udpate user query
#	delete user query
#	retrive user query


# C = Controller: handles the interaction of the user and pass the data to the model. (Waiter)
class User_Controller:

    def AddUser():
        while True:
            print("""
            What would you like to ADD:            
            1. Add First Name
            2. Add Last Name
            3. Add User Name
            4. Add Email Id
            5. Add Password
            """)

            add_info = int(input("Type the 1 to 5 to add the following information:"))
            if add_info == 1:
                first_name = str(input("Enter your first name:"))
                print("First Name Added")
            elif add_info == 2:
                last_name = str(input("Enter your last name:"))
                print("Last Name Added")
            elif add_info == 3:
                user_name = str(input("Enter your user name:"))
                print("User Name Added")
            elif add_info == 4:
                email_id = input("Enter your email id:")
                print("FEmail Id Added")
            elif add_info == 5:
                password = input("Enter your password:")
                print("Password Added")
            else:
                print("Enter number only from 1 to 5")

            close = str(input("Hit Enter to Add other information or type c to close."))
            if close == "C" or close == "c":
                break


    def UpdateUser():
        while True:
            print("""
            What would you like to Update:            
            1. Update First Name
            2. Update Last Name
            3. Update User Name
            4. Update Email Id
            5. Update Password
            """)

            add_info = int(input("Type the 1 to 5 to Update the information:"))
            if add_info == 1:
                first_name = str(input("Enter your first name:"))
                print("First Name Updated")
            elif add_info == 2:
                last_name = str(input("Enter your last name:"))
                print("Last Name Updated")
            elif add_info == 3:
                user_name = str(input("Enter your user name:"))
                print("User Name Updated")
            elif add_info == 4:
                email_id = input("Enter your email id:")
                print("Email Id Updated")
            elif add_info == 5:
                password = input("Enter your password:")
                print("Password Updated")
            else:
                print("Enter number only from 1 to 5")

            close = str(input("Hit Enter to Add other information or type c to close."))
            if close == "C" or close == "c":
                break


    def DeleteUser():
        while True:
            print("""
            What would you like to Delete:            
            1. Delete First Name
            2. Delete Last Name
            3. Delete User Name
            4. Delete Email Id
            5. Delete Password
            """)

            add_info = int(input("Type the 1 to 5 to Delete the information:"))
            if add_info == 1:
                first_name = str(input("Enter your first name:"))
                print("First Name Deleted")
            elif add_info == 2:
                last_name = str(input("Enter your last name:"))
                print("Last Name Deleted")
            elif add_info == 3:
                user_name = str(input("Enter your user name:"))
                print("User Name Deleted")
            elif add_info == 4:
                email_id = input("Enter your email id:")
                print("Email Id Deleted")
            elif add_info == 5:
                password = input("Enter your password:")
                print("Password Deleted")
            else:
                print("Enter number only from 1 to 5")

            close = str(input("Hit Enter to Add other information or type c to close."))
            if close == "C" or close == "c":
                break

    def RetrieveUser():
        print(User_Model.data)


# V = View: presentation of data from the Model to the user. (frontend) (customer)
"""import panda as pd

user_dictionary = {}
user_table = pd.DataFrame(user_dictionary)

dictionary = on_submit(Controller.add_user)
user_table = pd.DataFrame(dictionary)

print(user_table) 

"""

# Creating Menus


while True:
    print("""
    Menus
    Enter number 1 to 5 to do the following task:
    1. Create User
    2. Add User
    3. Update User
    4. Delete User 
    5. Retrieve User
    """)
    choose = int(input("Enter number:"))

    if choose == 1:
        # Asking user id and all info from the user
        choose_user_id = int(input("Create you user ID:"))
        first_name = str(input("Enter your first name:"))
        last_name = str(input("Enter your last name:"))
        user_name = str(input("Enter your user name:"))
        email_id = input("Enter your email id:")
        password = input("Enter your password:")

        #creating object for user model
        obj_of_User_Model = User_Model(choose_user_id)
        obj_of_User_Model.create(first_name, last_name, user_name, email_id, password)


    elif choose == 2:
        User_Controller.AddUser()
    elif choose == 3:
        User_Controller.UpdateUser()
    elif choose == 4:
        User_Controller.DeleteUser()
    elif choose == 5:
        User_Controller.RetrieveUser()
    else:
        print("Ener number form 1 to 5 only:")

    print("Hit Enter to continue to Menu or type c to close.")
    close = str(input())
    if close == "C" or close == "c":
        break
