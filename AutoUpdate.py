# Version 1.0.1 - (Updated version)
import random
import urllib
import filecmp
import string
import time
def Main():
    print "Hello,", usern + "!"

def autoUpdate():
    verFile = ("https://raw.githubusercontent.com/othertylerparker/PythonProject/master/AutoUpdate.py")
    file_name = verFile.split('/')[-1]
    file = open(file_name, 'r')
    u = urllib.urlopen(verFile)
    f = open("AutoUpdate.py", 'r')
    checkNew = u.readline()[0]
    checkOld = f.readline()[0]
    if checkOld == checkNew:
        print "Files match"
    else:
        print "Files do not match. Updating."
        file = open(file_name, 'wb')
        u = urllib.urlopen(verFile)
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            file.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8) * (len(status) + 1)
            print status,

        file.close()
        f.close()
while True:
    autoUpdate()
    with open('userpass') as f:
        try:
            menu=int(raw_input("""What would you like to do?
1. Register
2. Login
3. Reset Password
9. Quit
"""))
        except ValueError:
            print "Enter a number!"
            continue
        if menu == 1:
            user = raw_input("What would you like your username to be?: ")
            passw = raw_input("What would you like your password to be?: ")
            securecode = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(20))
            print "Your secure code is:", securecode + ". Use this if you forget your password. It is very important."
            f = open('userpass', "a")
            f.write(user + "~" + passw + "~" + securecode + "\n")
            print "Account successfully created!"
        if menu == 2:
            user = raw_input("What is your username?: ")
            passw = raw_input("What is your password?: ")
            credentials = [x.strip().split("~") for x in f.readlines()]
            for usern,passwo,securecod in credentials:
                if user == usern and passwo == passw:
                    print "Successfully Logged in!"
                    Main()
                else:
                    print "Error while logging in, please check username or password."
        if menu == 3:
            securecode = raw_input("What is your secure code?: ")
            credentials = [x.strip().split("~") for x in f.readlines()]
            secureCodes = False
            for usern,passwo,securecod in credentials:
                if securecode == securecod:
                    secureCodes = True
                    newpass = raw_input("What would you like your new password to be?: ")
                    with open('userpass', "r") as f:
                        filedata = f.read()
                    filedata = filedata.replace(passwo, newpass)
                    with open('userpass', "w+") as c:
                        c.write(filedata)
                        print "Password updated successfully!"
            if secureCodes == False:
                print "Secure code does not exist"
