import os 
import hashlib
import getpass

class User:
    def __init__(self, username, password_hash, salt, role , permission = "0"):
        self.username = username
        self.password_hash = password_hash
        self.salt = salt
        self.role = role
        self.permission = permission

class LoginUser:
    def __init__(self):
        self.users = []
        default_password_hash, default_salt = self._hash_password("admin")
        default_admin = User("admin", default_password_hash, default_salt, "admin")
        self.users.append(default_admin)
    def _hash_password(self, password, salt=None):
        if salt is None:
            salt = os.urandom(16).hex()
        salted_password = password + salt
        return hashlib.sha256(salted_password.encode()).hexdigest(), salt
    
            
    def register(self , username , password , role , permission="0"):
        if len(username) <3:
            raise ValueError("Username cant be this short")
        if len(password)<8:
            raise ValueError("The Password Should be over 8 letters")
        if role not in ("admin" , "manager" , "employee"):
            raise ValueError("The role must belong from (admin , manager , employee)")
        for user in self.users:
            if user.username == username:
                raise ValueError("User Already Exists")
        password_hash, salt = self._hash_password(password)
        new_user = User(username, password_hash, salt, role , permission)
        self.users.append(new_user)
        print(f"\nUser {username} registered successfully as {role}!")
        

    def login(self, username, password):
        for user in self.users:
            if user.username == username:
                if self._verify_password(password, user.password_hash, user.salt):
                    print(f"\nWelcome {username}! You're logged in as {user.role}.")
                    if user.role == "admin":
                        logged_in_user = Admin()
                        logged_in_user.admin_menu(self)
                    elif user.role == "manager":
                        logged_in_user = Manager(user.permission)
                        logged_in_user.admin_menu(self)
                        
                    elif user.role == "employee":
                        logged_in_user = Employee()
                        logged_in_user.view_tasks()
                    else:
                        print("\nInvalid role!")
                    return logged_in_user

        print("\nInvalid username or password!")
        return None
    def _verify_password(self, password, stored_hash, stored_salt):
        hashed_input , _ = self._hash_password(password, stored_salt)
        return hashed_input == stored_hash
    def delete_user(self , username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)
                print(f"The User {username} is removed")
                return
            
        print("User Not Found...Please Check Records")

#Previlages
class Admin:
    def __init__(self , permission = "0"):
        self.role = "admin"
        self.permission = permission

    def admin_menu(self, auth_system):
        """Display Admin Menu and handle admin-specific tasks."""
        while True:
            print("\n--- Admin Menu ---")
            print("1. Register a User")
            print("2. View Records")
            print("3. Delete a User")
            print("4. Give Permissions")
            print("5. Exit To main Menu")

            choice = input("Select an Option: ")

            if choice == "1":
                print("\n=== Register a User ===")
                username = input("Enter Username: ")
                password = getpass.getpass("Enter Password: ")
                role = input("Enter The Role (admin / manager / employee): ").lower()
                try:
                    auth_system.register(username, password, role)
                except ValueError as e:
                    print(f"\nError: {e}")
            elif choice == "2":
                print("\n=== Registered Users ===")
                for user in auth_system.users:
                    print(f"Username: {user.username}, Role: {user.role}")
            elif choice == "3":
                username=input("Enter The User Name : ")
                auth_system.delete_user(username)
            elif choice == "4":
                username = input("Enter The Manager's Username: ")
                for user in auth_system.users:
                    if user.username == username and user.role == "manager":
                        permission = input("Grant Super Permission? (1 for Yes, 0 for No): ")
                        user.permission = permission
                        print(f"\nSuper Permission {'Granted' if permission == '1' else 'Revoked'} for Manager {username}.")
                        return
                print("\nManager not found!")
 
            elif choice == "5":
                print("\nExiting Admin Menu...")
                break
            else:
                print("\nInvalid Option. Please try again.")

class Manager(Admin):
    def __init__(self, permission="0"):
        self.role = "manager"
        super().__init__(permission)

    def admin_menu(self, auth_system):
        """Manager menu with restricted privileges by default."""
        while True:
            print("\n--- Manager Menu ---")
            print("1. Register an Employee")
            print("2. View Records")
            if self.permission == "1":  # Additional options if super permission is granted
                print("3. Register Any User")
                print("4. Delete a User")
            print("5. Exit To Main Menu")

            choice = input("Select an Option: ")

            if choice == "1":
                print("\n=== Register an Employee ===")
                username = input("Enter Employee Username: ")
                password = getpass.getpass("Enter Password: ")
                role = "employee" 
                try:
                    auth_system.register(username, password, role)
                except ValueError as e:
                    print(f"\nError: {e}")

            elif choice == "2": 
                print("\n=== Registered Users ===")
                for user in auth_system.users:
                    print(f"Username: {user.username}, Role: {user.role}")

            elif self.permission == "1" and choice == "3":
                print("\n=== Register Any User ===")
                username = input("Enter Username: ")
                password = getpass.getpass("Enter Password: ")
                role = input("Enter The Role (admin / manager / employee): ").lower()
                try:
                    auth_system.register(username, password, role)
                except ValueError as e:
                    print(f"\nError: {e}")

            elif self.permission == "1" and choice == "4":  # Delete a User (Requires permission)
                username = input("Enter The User Name to Delete: ")
                auth_system.delete_user(username)

            elif choice == "5":  # Exit Menu
                print("\nExiting Manager Menu...")
                break

            else:
                print("\nInvalid Option. Please try again.")

class Employee:
    def __init__(self):
        self.role = "employee"

    def view_tasks(self):
        print("Employee can view tasks and submit work reports.")

def main():
    auth_system = LoginUser()
    while True:
        print("1. Login")
        print("2. Exit")
        choice = input("Select an Option : ")
        if choice == "1":
            print("===Please Login Your Account===")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            auth_system.login(username, password)
        elif choice == "2":
            print("Exiting......GoodBye!")
            break
        else:
            print("Invalid Option")
main()