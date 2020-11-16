'''
Trainiton Analytics
-+-+-+-+-+-+-+-+-+-

AIM:
---
Write a login program. This should be a program that prompts the user for their
username and password. If the user enters the right predetermined password, they are
logged into the system otherwise, the program should ask them to re-enter the
password. The user can only get 5 trials to enter the correct password, after which the
program should tell them that they are kicked off the system and the username
blacklisted. The program will then prompt for a username and if it is a blacklisted
username, it will show an error and state that the username is blacklisted.

Intern: Franklin Obasi
'''

print("Welcome To Admin Login")

#usernames = ['Frank111', '001Ade', 'Honey5']
#passwords = ['2345', '5678', 'f55p']
login = [['Frank111','2345'],
         ['001Ade','5678'],
         ['Honey5','f55p']]

black_list = ['bola3']

validator = False
trial = 5

while not validator:
    if trial < 5 : print(f"You have {trial} trial(s) left")
    print()  
    print("Enter your username :")
    username = input()
    print()
    
    if username in black_list:
        print("Error!")
        print(f"{username} have been blacklisted, {username} have no access to this server")
        trial = 5
        continue
    
    print("Enter your password : ")
    password = input()
    print()
    
    if [username, password] in login:
        print("Access granted!")
        validator = True
    else:
        trial -= 1
        if trial == 0:
            print("Trial limit exceeded!")
            print("Unfortunately, we have suspected you to be a robot")
            black_list.append(username)
            trial = 5
            continue
        print("Incorrect login details!")
        print("Check your username and password, then try again!")

    
        
        

















        

    
