
class Stock:
    def __init__(self,company_name, symbol):
        self.__company_name = company_name
        self.__symbol = symbol
    def get_symbol(self):
        return self.__symbol
    def get_company_name(self):
        return self.__company_name

def create_list(file_name):
    stock_data = ['Symbol Company','AAPL Apple_Inc',
'CAT Caterpillar',
'EK Eastman_Kodak',
'GOOG Google',
'MSFT Microsoft']

    out_file = open(file_name,'w')
    for set in stock_data:
        out_file.write(set + '\n')

    out_file.close()

def get_stock_list(file_name):
    dict= {}
    in_file = open(file_name, 'r')
    
    for line in in_file:
        symbol, company_name = line.strip().split(' ', 1)
        stock = Stock(company_name, symbol)
        dict[company_name] = stock

    in_file.close()
    
    return dict
