from random import seed
from random import randint
from itertools import groupby

def sumArray(arr):
    sum = 0
    for i in arr: 
        sum = sum + i 
          
    return(sum)

def bigEArray(arr):
    max = arr[0]

    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i]

    return max

def findObject(array, find):
    for i in range(len(array)):
        if array[i]["name"] == find:
            return i
    return -1

def initGr():
    onTheSpace = ""
    matrixMain = []
    whileLoop = 0
    matrixHeader = input("Hãy nhập đỉnh của ma trận cách nhau bằng khoảng trống (phím space). Nhập xong nhấn Enter\n").strip().split(" ")
    print("Hãy nhập ma trận tam giác của bạn, nhập xong 1 dòng ấn Enter. Nhấn Enter 2 lần để duyệt ma trận (ví dụ: 0 1 1 0)")
    while True:
        if len(matrixMain) == len(matrixHeader):
            break
        matrixRaw = input(onTheSpace)
        myMatrix = matrixRaw.strip().split(" ")
        if len(myMatrix) == 1 and myMatrix[0] == '':
            myAnswer = input("Bạn đã nhập xong ma trận? [Y/N]")
            if myAnswer.lower() == "y":
                break
        else:
            matrixMain.append(myMatrix)
            onTheSpace += "  "
    formatGr(matrixMain, matrixHeader, matrixMain + [])

def formatGr(matrixInput, matrixHeader, fullMatrix):
    browser = 0
    outputMatrix = []
    while True:
        if len(outputMatrix) == len(matrixInput):
            break
        if browser == 0:
            outputMatrix.append(sumArray(list(map(int, matrixInput[0]))))
        else:
            var = browser
            loop = 0
            total = 0
            tempArr = []
            while var > 0:
                total += int(matrixInput[loop][var])
                tempArr.append(matrixInput[loop][var])
                var -= 1
                loop += 1
            outputMatrix.append(total + sumArray(list(map(int, matrixInput[browser]))))
            fullMatrix[browser] = tempArr + matrixInput[browser]
        browser += 1
    for i in range(0, len(fullMatrix)): 
        for j in range(0, len(fullMatrix[i])): 
            fullMatrix[i][j] = int(fullMatrix[i][j])
    startProgressCl(fullMatrix, matrixHeader)

def isSafe(arrayMain, v, colour, c, matrixHeader):
    for i in range(len(matrixHeader)):
        colour[v] = 0
        if arrayMain[v][i] == 1 and colour[i] == c:
            return False
    return True

def grColourUtil(arrayMain, colour, v, matrixHeader, emptyMe):
    if v == len(matrixHeader):
        return True
    for c in range(1, len(matrixHeader)):
        if isSafe(arrayMain, v, colour, c, matrixHeader) == True:
            colour[v] = c
            emptyMe.append({"name": matrixHeader[v], "color": c})
            if grColourUtil(arrayMain, colour, v+1, matrixHeader, emptyMe) == True:
                return True
            colour[v] = 0

def grColouring(arrayMain, matrixHeader):
    colour = [0] * len(matrixHeader)
    emptyMe = []
    if grColourUtil(arrayMain, colour, 0, matrixHeader, emptyMe) == False:
        return False

    return emptyMe

def startProgressCl(arrayMain, matrixHeader):
    result = grColouring(arrayMain, matrixHeader)
    finishGr(result)

def finishGr(inputArray):
    groups = groupby(sorted(inputArray, key=lambda a: a['color']), lambda a: a['color'])
    for key, group in groups:
        print("Color ID: %s, List: %s" % (key, list(group)))

def main():
    initGr()
    quit(0)

if __name__ == "__main__":
  main()
