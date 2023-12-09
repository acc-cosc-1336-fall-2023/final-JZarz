import question_c
def menu():
    opt = input('Would you like to find the Contiguous collection between two strings? \n type 1 for yes\n type 2 to Exit: ')

    if opt != '2':
        if opt == '1':
            cont_collection()
            
        elif opt != '1':
            print('invalid')
    else:
        print('Exiting')
def cont_collection():
    print('Find the contiguous collection between two strings')
    str1 = input("create a string that is between 8 to 16 characters long: ")
    str2 = input("create a second string that is 4 characters long: ")

    if len(str1) >= 8 and len(str1) <= 16 and len(str2) == 4:
        num = question_c.get_most_likely_ancestor(str1.upper(), str2.upper())
        print(f'The contiguous collection can be found at {num}')
        cont()
    else:
        print('Invalid strings')

def cont():
    ans = input('would you like to find another?\n type Y to try again\n type N to exit: ')
    if ans.upper() != 'N':
        if ans.upper() == 'Y':
            cont_collection()
        elif ans.upper() != 'Y':
            print('invalid')
    else:
        print('Exiting')

menu()
