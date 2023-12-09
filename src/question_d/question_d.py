class Stock:
    def __init__(self,company_name, symbol):
        self.__company_name = company_name
        self.__symbol = symbol
    def get_symbol(self):
        return self.__symbol
    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    
    symbol_stock = Stock('Symbol', 'Company')
    appl_stock = Stock('APPL', 'Apple_Inc')
    cat_stock = Stock('CAT', 'Caterpillar')
    ek_stock = Stock('EK', 'Eastman_Kodak')
    goog_stock = Stock('GOOG', 'Google')
    msft_stock = Stock('MSFT', 'Microsoft')
    dict = {'Symbol': symbol_stock, 'APPL': appl_stock, 'CAT': cat_stock, 'EK': ek_stock, 'GOOG': goog_stock, 'MSFT': msft_stock}
    
    for symbol, stock in dict.items():
        print(f'{stock.get_symbol().ljust(16)} {stock.get_company_name().ljust(6)}' )

