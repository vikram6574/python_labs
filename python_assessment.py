#Print “Hello World!” to the terminal

print ("Hello World!")    

#Create a variable with a number and print the variable to the screen

x = 5
print (x)

#Get the user to input a float number and convert to an integer

y = float(input("Enter a number "))
print(int(y))   



#Create if else statement to see if user likes dogs

dogs = input("Do you like dogs? ")
if dogs == "yes":
    print("You like dogs")
else:
    print("You don't like dogs")
    
    
#Create while loop to go as long as user input is not 5

while True:
    x = int(input("Enter a number "))
    if x == 5:
        break
    else:
        print(x)    
        
        