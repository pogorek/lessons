
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

tableDataRowsLen = len(tableData)

def printTable():

    result = ""
    tableDataLen = []
    for i in range(tableDataRowsLen):
        tableDataLen.append(len(max(tableData[i], key=len)))

        for j in range(len(tableData[i])):
            tableData[i][j] = tableData[i][j].rjust(tableDataLen[i])

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            result += tableData[j][i] + " "

        result += "\n"

    print(result)

printTable()
