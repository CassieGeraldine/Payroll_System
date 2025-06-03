# #Break statement:
# numbers = [1,3,4,5,6]

# #I am  going to find the first odd number in the list:
# for number in numbers:
#     if number % 3 == 0:
#         print(f"The first odd number is:{number}")
#         break


# #Continue statement:
# numbers = [1,3,4,5,6]

# #I am  going to skip the odd numbers in the list:
# for number in numbers:
#     if number % 3 == 0:
#         #print(f"The first odd number is:{number}")
#         continue
#     print(number)

#...............................................................................
# #LISTS:

# my_numbers = [2,3,4,"Cassie",True,8]
# print(my_numbers[-3])


# a = [1,2,3]
#b = ["Cassie is awesome", 4,5,"whatever"]

# print("string conctenation")
# print(a+b)
# print(a * 4)

# print("len, min and max")
# print(len(a))
# print(max(a))
# print(min(a))

# #List Methods:

#Append

# print("append")
# names = ["Cassie", "Scotty"]
# names.append("Genius")
# print(names)

# #Insert
# print("insert")
# b.insert(3,"Chill")
# print(b)

# # .remove
# print("remove")
# b.remove("whatever")
# print(b)

# # .pop
# print("pop")
# b.pop(2) #removes an element at index 2.(count from 0)
# print(b)

# # #index
# print("Index and pop.")
# print(b.index(4))

# o = input()
# b.pop(b.index(o))
# print(b)
#pop returns a values, so you can choose to store it in a variable inorder to see what you're popping.

# age = [23,50,24, 35, 26,22,42]
# age.sort()
# print(age) #sorts in ascending order.

# # or you can use the sorted method
# print(sorted)
# nums = [5,3,1,6]
# print(sorted(nums))

#......................................................
# #  TUPLES:

# my_tuple = (1,2,3,4,5)

# #1st typecast it to a string
# new_tuple = list(my_tuple) #pass the name of the variable/list
# new_tuple[2] = 15

# #you can change it back to a tuple if you do not want it to be changed.
# new_tuple = tuple(new_tuple)
# print(new_tuple)

#.......................................................
#DICTIONARIES:

# my_dict = {"name":"Cassandra", "age":13, "gender":"female"}
# print(my_dict["name"])

# my_dict["occupation"] = "student" #addding a key, value pair.
# print(my_dict)



#dictionary returns to you alist, then u can choose which list methods to use on them.
# print("keys")
# li = my_dict.keys()
# print(f"{li}\n")
# for names in li:
#     print(names)

# print("items")
# print(f"{my_dict.items()}\n")
# items_in_dictionary = tuple(my_dict.items())
# values = list(my_dict.values())


# for key, value in my_dict.items():
#     i = values.index(value)
#     item = items_in_dictionary[i]
#     print(f"tuple: {item}" )
#     print(key ,":", value)


# robots = {"aimbot":["betty","fast",8],"club":["bob","slow",8]}

# name = input("Enter a robot name: ")
# values = input("Access attribute: a: name,b: speed,c: height")

# for key,value in robots.items():
#     if key == name:

#         if values == 'a':
#             print(value[0])  #Name
#         elif values == 'b':
#             print(values[1])   #Speed
#         elif values == 'c':
#             print(values[2])   #height



# print("values")
# print(f"{my_dict.values()}\n")





# #..................
# a = [1,2,3]

# print(1 in a)
# print(6 not in a)

#=====================================================================
# print(2**5)
# print(10//3)
# print(10/3)
# print(10%3)
# print(-10//3)


# x = 5
# y = 10

# if x>= y:
#     print("smaller")
# else:
#     print("bigger")

# num=10

# while  num <= 5:
#     print("Greater")
#     break
# else:
#     print("smaller")


# def find_average(*numbers):
#     """Find the average of a list of numbers int the list 'numbers' and return
#     it as a float to one decimal point"""

#     #numbers = [] #for storing up numbers and sum them up later.
#     my_sum = 0 #need to initialize sum to 0, so that we can have a base to add to.


#     for num in numbers:
#         #numbers.append(num)
#         my_sum += num

#     return my_sum

# print(find_average(2,3,4))


# def number():
#     number = int(input("Enter a number: "))
#     if number % 2 == 0:
#         print("this is an even number")
#     else:
#         print("This is not an even number.")


# number()

#=================================================================
#PROBLEM 1:
# for i in range(1,11,3):
#     print(i,end=" ")

# PROBLEM 2:
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# PROBLEM 3:
#Problem: Write a program that calculates and
# prints the sum of numbers from 1 to 10.
# sum = 0

# for i in range(1,11):
#     sum+= i

# print(sum)

# PROBLEM 4:

# Multiplication Table of a Number
# Problem: Ask the user for a number and print its multiplication table up to 10.
# Example: If the user enters 5, the output should be:
# 5 x 1 = 5
# 5 x 2 = 10

def user_input():
    number=int(input("Enter Number: "))
    print(f"You entered: {number}")


#def Multiplication_Table():



if __name__== "__main__":
    user_input()
