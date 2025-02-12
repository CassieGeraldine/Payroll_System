#dealing with a break statement:
numbers = [1,3,4,5,6]

#I am  going to find the first odd number in the list:
for number in numbers:
    if number % 3 == 0:
        print(f"The first odd number is:{number}")
        break


#dealing with a Continue statement:
numbers = [1,3,4,5,6]

#I am  going to skip the odd numbers in the list:
for number in numbers:
    if number % 3 == 0:
        #print(f"The first odd number is:{number}")
        continue
    print(number)

    
