import question_d

def menu():
    ans = input('select choice\n 1. Display stock purchase history \n 2. Exit: ')
    if ans != '2':
        if ans =='1':
            opt1()
        elif ans != '1':
            print('invalid')
    else:
        print('exiting')

def opt1():
    print('Displaying Stock Purchase History')
    history = question_d.stock_purchase_history()
    print(history)
    cont()

def cont():
    ans = input('select option\n 1. Display stock purchase history \n 2. Exit: ')
    if ans != '2':
        if ans == '1':
            opt1()
        elif ans != '1':
            print('invalid')
    else:
        print('exiting')

menu()