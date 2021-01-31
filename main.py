from getpass import getpass
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

UserName = input("Pleas Enter Your Name : ")
Password = getpass("Pleas Enter Your Password : ")

if UserName == "F14Commander" and Password == "1313" :
    print("welcome")
else:
    exit("Error")