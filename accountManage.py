from tkinter import *
loggedIn = False
name = None
def signup():
    global loggedIn, name
    name = input("What do you want to be your username?")
    if " " in name:
        print('Sorry, you are not allowed to have spaces in your username')
        main()
    nameCheck = name.lower()
    usernames = open('usernames','r')
    allUsers = usernames.readline().lower()
    allUsers = allUsers.split(" ")
    #for loop checks to see if someone already has name
    for x in allUsers:
        if nameCheck == x:
            print("Sorry, someone already has that username")
            main()
    password = input("What do you want your pasword to be?")
    user = open(name,'w')
    user.write(name + '\n')
    user.write(password)
    print("Thank you for signing up!")
    usernames.close()
    user.close()
    allUsers.append(name)
    usernames = open('usernames','w')
    usernames.write(" ".join(allUsers))
    usernames.close()
    loggedIn = True

def login():
    global loggedIn, name
    name = input("What is your username?")
    usernames = open('usernames','r')
    allUsers = usernames.readline()
    allUsers = allUsers.split(" ")
    check = False
    for x in allUsers:
        if x == name:
            check = True
    if not check:
        print("I'm sorry, there is no user with the name",name)
        main()
    user = open(name, 'r')
    useless = user.readline()
    password = user.readline()
    askP = input("What is your password?")
    if askP == password:
        main_window = Tk()
        text = Label(main_window, text='Welcome, ' + name + '!', background='green',
                     foreground='red', font='Times 20', relief='groove', borderwidth=10)
        text.grid(row=0, column=0)
        quitB = Button(main_window, text='Quit',command=main_window.destroy)
        quitB.grid(row=1,column=0)
        mainloop()
        loggedIn = True
    else:
        print("I'm sorry, that was not the correct password")
        main()
def logout():
    ask = input("Are your sure you want to log out? If you want to, type in LOGOUT").upper()
    if ask == 'LOGOUT':
        loggedIn = False;
        print('logged out')
    else:
        print('you did not log out')
def main():
    welcome = input('Welcome! If you have already signed up, type in LOGIN. If you have not signed up, type in SIGNUP').upper()
    if welcome == 'LOGIN':
        login()
    elif welcome == 'SIGNUP':
        signup()
    else:
        print("Please type in either LOGIN or SIGNUP")
        main()
main()
