import os


dir = os.getcwd()

def reutrnUserID():
    print(os.geteuid())

def operating_system_info():
    print(os.uname())


print(dir)
reutrnUserID()
operating_system_info()