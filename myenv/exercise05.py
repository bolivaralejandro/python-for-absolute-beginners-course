#number = int(input("Enter a number: "))
number =''
while number != 0:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    elif number %2 == 0:
        print("Even")
        continue
    #elif number %3 == 0:
    #    print("Odd")
    else:
        print("Odd")
        continue
print("Goodbye")    
