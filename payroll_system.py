#Reminder on how to use that cheat sheet

#three separate lists.
list_of_emp_names =['Tom','Edwin','Josh']
list_of_surnames =['Baily','Bark','Wolf']
list_of_employee_numbers = ['00635','87958','09783']

#Print function
def greetings():
    print("WELCOME TO KASSIDY PAYROLL SYSTEM")
    print("MENU:")


#View employees
def view():
    for index,surname in enumerate(list_of_surnames):
        print(f" {index + 1}) {list_of_emp_names[index]} {surname} {list_of_employee_numbers[index]}")


    # for i in range(len(list_of_emp_names)):
    #     print(list_of_emp_names[i]+ " "+list_of_surnames[i]+ " "+(str(list_of_employee_numbers[i])))

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

    # print("List of names:")
    # #Enumerate shows the index number and the name.
    # for i, name in enumerate(list_of_emp_names):
    #     print(f"{i + 1}:{name}")

    # delete_name = input("Delete name?")
    # #Coverted the input into an interger because the input function only takes strings.
    # new_del_name = int(delete_name)
    # del list_of_emp_names[new_del_name-1]

    # print(list_of_employee_numbers)

    # for name in list_of_emp_names:
    #     print(name)

    """_deleting by surname_
    """
    print("=========================================")
    print("List of employee surnames")
    #prints the lists of surnames and their index numbers.
    for index,surname in enumerate(list_of_surnames):
        print(index + 1,surname)

    #remember the input function only takes in strings,
    #so if i want the user to choose a number I have to convert
    #whatever they
    delete_surname = input("Delete surname:")
    new_del_surname = int(delete_surname)




    print("=========================================")


    #first have to convert

def update_employee():
    update_emp_name= input("Enter employee name you want to update")
    list_of_emp_names.update()

    update_emp_surname = input("Enter employee surname you want to update")
    list_of_surnames.update()

    update_emp_number= input("Enter employee number you want to update")
    list_of_employee_numbers.update()

    print(list_of_emp_names)
    print(list_of_surnames)
    print(list_of_employee_numbers)


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

        option=input("What would you like to do?")

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
            update_employee()
        elif option == "5":
            #Calling the function to quit the program.
                exit_program()



if __name__ == "__main__":
    menu()
    # help(list)  , when you need help about a certain topic.
