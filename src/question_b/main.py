import  question_b

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
    stock_dict = question_b.get_stock_list('stocklist.txt')
    for symbol, stock in stock_dict.items():
        print(f'{stock.get_company_name().ljust(16)} {stock.get_symbol().ljust(6)}')
    
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