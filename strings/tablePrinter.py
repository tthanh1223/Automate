
# print in the following:
# apple        blue     one
# orange        red     two
# strawberry    pink    five
# banana        yellow  twelve
# with each-column right-justified.
def printTable(table_data):
    colWidths = [0] * len(table_data)
    for i in range(len(table_data)):
        largest_length = 0
        for j in range(len(table_data[i])):
            if len(table_data[i][j]) > largest_length:
                largest_length = len(table_data[i][j])
        colWidths[i] = largest_length
    rows = []
    for j in range(len(table_data[0])):
        rows.append([table_data[i][j] for i in range(0,len(table_data))])
    for index_row in range(len(rows)):
        for index_word in range(len(rows[index_row])):
            print(rows[index_row][index_word].rjust(colWidths[index_word]), end=" ")
        print()

table_data_1 = [['apples','orange','strawberry','banana'],
              ['blue','red','pink','yellow'],
              ['one','two','five','twelve']]
printTable(table_data_1)
table_data_2 = [
    ['apples', 'orange', 'strawberry', 'banana', 'kiwi', 'grape', 'watermelon'],
    ['blue', 'red', 'pink', 'yellow', 'green', 'purple', 'dark green'],
    ['one', 'two', 'five', 'twelve', 'three', 'seven', 'eight'],
    ['small', 'medium', 'large', 'medium', 'small', 'large', 'huge']
]

printTable(table_data_2)

