# Programmit By Suliman Almohawis | TWitter : F14Commander

from getpass import getpass # getpass libery we uset for get The password

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

UserName = input("Pleas Enter Your Name : ") # Get UserName
Password = getpass("Pleas Enter Your Password : ") # Get The Password

# Edit The Username or Password and write Your Username And Password
if UserName == "F14Commander" and Password == "1313" :
    print("welcome") # Her i Print Welcome You can write {pass}
else:
    exit("Error") # Her i write {exit} for Exit The Program

