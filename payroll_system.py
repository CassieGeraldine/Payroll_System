#Reminder on how to use that cheat sheet

#three separate lists.
list_of_emp_names =['Tom','Edwin','Josh']
list_of_surnames =['Baily','Bark','Wolf']
list_of_employee_numbers = ['00635','87958','09783']

#Print function
def greetings():
    print("=========================================")
    print("WELCOME TO KASSIDY PAYROLL SYSTEM")
    print("MENU:")
    print("=========================================")


#View employees
def view():
    for index,surname in enumerate(list_of_surnames):
        print(f" {index + 1}) {list_of_emp_names[index]} {surname} {list_of_employee_numbers[index]}")


def add_new_employee():
    """
        Need to add new employees into three separate lists
        name, surname, employee_number.
    """
    employee_name=input("Enter name:")
    list_of_emp_names.append(employee_name)

    employee_surname=input("Enter surname:")
    list_of_surnames.append(employee_surname)

    new_employee_number=input("Enter employee number:")
    list_of_employee_numbers.append(new_employee_number)

def delete_employee():

    print("=========================================")
    print("List of names:")
    #Enumerate shows the index number and the name.
    for i, name in enumerate(list_of_emp_names):
        print(f"{i + 1}:{name}")

    delete_name = input("Delete name?")
    #Coverted the input into an interger because the input function only takes strings.
    new_del_name = int(delete_name)
    del list_of_emp_names[new_del_name-1] #-1 so that the index number can start from 0, cause
    #we incremented when we were printing the list, so that the user does not see the first
    # name printed on option 0, however when we now want to delete the first index we have to
    #decrement the index by 1 so that it matches.

    print("Remaining employee names")
    for name in list_of_emp_names:
        print(name)

    """_deleting by surname_
    """
    print("List of employee surnames")
    #prints the lists of surnames and their index numbers.
    for index,surname in enumerate(list_of_surnames):
        print(f"{index + 1}:{surname}")

    delete_surname = input("Delete surname:")
    new_del_surname = int(delete_surname)
    del list_of_surnames[new_del_surname-1]

    print("Remaining employee surnames")
    for surname in list_of_surnames:
        print(surname)

    """Deleting by employee numbers.
    """
    #Displaying employee number and incremented the index number so that the user can see it starting from 1 instead of 0.
    print("Employee Numbers:\n")
    for num_index,number in enumerate(list_of_employee_numbers):
        print(f"{num_index + 1}:{number}")

    delete_emp_number=input("Select employee number to delete.")
    del list_of_employee_numbers[int(delete_emp_number)-1]

    print("Remaining employee numbers:")
    for num in list_of_employee_numbers:
        print(num)

    print("=========================================")


def exit_program():
    outcome = input("Do you want to quit?  YES/ NO")
    if outcome!= 'NO':
        print("Goodbye")

#Calling all the functions inorder to create a menu.
def menu():

    #Calling the greetings function.
    greetings()

    while True:

        print("1) View employees")
        print("2) Add an employee")
        print("3) Delete an employee")
        print("4) Update an employee")
        print("5) Quit")

        option=input("What would you like to do?\n")

        if option == "1":
        #Calling the View function
            view()
        elif option == "2":
            #Calling the AddEmployee function.
            add_new_employee()
        elif option == "3":
            #Calling the delete function
            delete_employee()
        elif option == "4":
            #Calling the update function
            add_new_employee()
        elif option == "5\n":
            #Calling the function to quit the program.
            exit_program()



if __name__ == "__main__":
    menu()
    # help(list)  , when you need help about a certain topic.
