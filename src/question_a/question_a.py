#write functions here, don't add input('') statements here!
def test_config():
    return True

def create_multiplication_table(num1, num2):
    table = []
    i = 0
    while i < num1:
        row = []
        j = 0
        while j < num2:
             product = (i+1)*(j+1)
             row.append(product)
             j += 1
        table.append(row)
        i += 1
    return table

def display_multiplication_table(table):

    for row in table:
        for ch in row:
            print(str(ch), end= ' ')
        print('\n')