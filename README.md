# Role-Base-access-control-
Role Base access control mock project 
Key Features 
    -Login System
        -Passwords are encrypted with hashible technique
        -If two passwords are same it include a Salt in one of them so two hashible passwords cant be the same
        -passwords should be greater than 8
        -two users with same username cant register
        -Admin Id password is admin,admin by default Hardcoded
        -Passwords are not visible when typing in cli with the help of getpass library 
Admin Privileges
    -Register a user (admin , manager , employee)
    -view registered employees
    -delete a employee profile 
    -Give super-permission to any manager(if there are two or more)
Manager Privileges
    -By default
        -Add a employee
        -View registered Employees
    -With Super-Permission
        -Add any User
        -Can Delete a User
Employee Privileges
    -View Tasks
    -Submit Tasks(Not Implemented) 
