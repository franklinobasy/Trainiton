'''
	Trainiton Analytics
	+-+-+-+-+-+-+-+-+-+-+
	
	AIM:
	------
	
	You are to write a program that prompts the user for a 
	height in feet and converts this input to meters. 
	This input can either be an integer or a float. Whenever 
	the user enters a height below zero (0), the program 
	should tell them that their entry is invalid and then 
	ask them to enter a new height. 
	This code should run as many times as possible. 
	This is a code that ensures that the correct type of value 
	is obtained in an input. It is necessary to obtain correct 
	value types in data collection to reduce the occurrence 
	of unclean data in the final dataset. 
	
	Intern: Franklin Obasi
'''


print("\tUnit Converter\t\t\t\t")
print("This is a unit converter that converts user's input in feet(ft) to meters(m)")
#set a flag, to control while loop that validates user input
validator = True

while validator:
    #prompt user to input request in foot(ft)
    print("\n\nEnter a number in foot :")
    request = float(input())


    if request >= 0:
        # 1 foot = 0.30480 meter
        # x feet =  0.30480 * x meters
        result = 0.30480 * request
        print("{0:0.4f} ft = {1:0.4f} m".format(request, result))
        
        print("\n\nEnter 'Y' to continue, or anyother key to quit")
        proceed = input()
        
        if proceed.upper() == 'Y':
            pass
        else:
            print("Unit converter gas stopped!")
            validator = False
        
    else:
        print(f"\n\nYour input is  {request} ft")
        print("The program doesn't work with request lower than 0")
        
        print("Enter 'Y' to continue, or anyother key to quit")
        proceed = input()
        if proceed.upper() == 'Y':
            print("Try again please!")
            pass
        else:
            print("Unit converter gas stopped!")
            validator = False
