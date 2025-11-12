"""Write some code using what you've learnt about the module operator
and conditional checks in Python to check if the number in the input area
is odd or even. If it's odd print out the word "Odd", otherwise print "Even" """

print("___Odd or Even checker, let's start!___")

number = int(input("Please type an integer number: "))

if number % 2 == 0:
    print("Even")

else: 
    print("Odd")

