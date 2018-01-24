def Register():
    f = open("logn.txt", "a")
    usern = raw_input("What would you like your username to be?: ")
    passw = raw_input("What would you like your password to be?: ")
    passwconf = raw_input("Please confirm your password: ")
    if passw == passwconf:
        f.write(usern + "~" + passw + "\n")
    else:
        print "Passwords do not match"
        Register()
def Login():
    f = open("logn.txt", "r")
    usern = raw_input("What is your username?: ")
    passw = raw_input("What is your password?: ")
    credentials = [x.strip().split("~") for x in f.readlines()]
    for username,password in credentials:
        if usern == username and passw == password:
            print "Success"
        else:
            print "Failure (like me)"
def Menu():
    while True:
        choice = int(raw_input("""What would you like to do?
1. Register
2. Login
"""))
        if choice == 1:
            Register()
        elif choice == 2:
            Login()
        else:
            print "Invalid choice!"
Menu()