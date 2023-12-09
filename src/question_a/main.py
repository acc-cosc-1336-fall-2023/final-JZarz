import question_a


def menu():
    choice = input("select an option:\n 1. Create a multiplication table\n 2. Exit: ")
    if choice != '2':
        if choice =='1':
            option_1()
        elif choice != '1':
            print('invalid choice')
    else:
        print('Exiting')    

def option_1():
    print('choose 2 numbers you would like to create the multiplication table with')
    num1 = int(input('First number: '))
    num2 = int(input('second number: '))
    table = question_a.create_multiplication_table(num1,num2)
    question_a.display_multiplication_table(table)
    cont()

def cont():
    ans = input('Would you like to create a new table?\n Type Y to create a new table\n Type N to exit: ')
    if ans.upper() != 'N':
        if ans.upper() == 'Y':
            option_1()
        elif ans.upper() != 'Y':
            print('invalid option')
    else:
        print('Exiting')

menu()
