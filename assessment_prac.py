# 13 February 2025.

#Dictionaries and Lists:

# Takes names ,ages and ID_number of 5 students and stores them in a dictionary.
# Prints out the dictionary.
# Finds and prints the oldest student’s name.

#problem breakdown:
# 5 students (for loop to iterate 5 times)
#user input to take name and age then store it in a dictionary.

#will first take them and store them in a list let's see:
#then make the first list a key and the other two lists values.


#Initial Approach.
# def get_name_age_ID():
#     names = []
#     for i in range(1,6):
#         name = input("Enter name: ")
#         names.append(name)
#     print(names)

#     Students_age = []
#     for age in range(1,6):
#         age = input("Enter age: ")
#         Students_age.append(age)
#     print(Students_age)

#     Students_ID = []
#     for J in range(1,6):
#         id_num = int(input("Enter ID Number: "))
#         Students_ID.append(id_num)
#     print(Students_ID)

# def get_name_age_ID():
#     students = {}

#     for i in range(1,2):
#         name = input("Enter name: ") #name has to be only letters

#         while True:
#             if name.isalpha():
#                 break
#             else:
#                 print("Name should only consist of letters.")

#         age = input("Enter age: ") # has to be only numbers
#         while True:

#             if age.isdigit():
#                 break
#             else:
#                 print("Age can only be a number.")
#                 break

#         id_num = input("Enter ID Number: ") #has to be only numbers and == of 5.
#         while True:
#             if id_num.isdigit() and len(id_num) == 5:
#                 break
#             else:
#                 print("Id can only be 5 numbers and == 5")
#                 break

#         students[name]=(age , id_num)
#         #students[name]=id_num

#     print(students)

#28 February 2025:
# working with data structures:

# Count occurrences of an element in a list.
# Write a function that counts how many times a given element appears in a list.

def number_input():
    number = input("Enter number to check it's occurence: ")
    return number

def occurences(check_num):
    print(f"You entered: {check_num}")
    pass

def main():
    # get_name_age_ID()
    check_num = number_input()
    occurences(check_num)


if __name__=="__main__":
    main()
