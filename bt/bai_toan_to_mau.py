## Lê Song Vĩ
## MSSV: 1811061712

from itertools import groupby
from re import match, compile

def sumArray(arr):
    sum = 0
    for i in arr: 
        sum = sum + i 
          
    return(sum)

def bigEArray(arr):
    max = arr[0]

    for i in range(len(arr)):
        if(arr[i].total > max.total):
            max = arr[i]

    return max

def initGr():
    spaceInf = ""
    matrixMain = []
    whileLoop = 0
    while True:
        matrixHeader = input(
            "Hãy nhập đỉnh của ma trận cách nhau bằng khoảng trống (phím space). Nhập xong nhấn Enter\n"
            ).strip().split(" ")
        if len(matrixHeader) == 1:
            matrixHeader = [i for i in matrixHeader[0]] if len(matrixHeader[0]) > 1 else []

        if len(matrixHeader) < 1:
            print("Đỉnh không hợp lệ")
        else:
            break;
    print(
        "Hãy nhập tam giác ma trận của bạn, nhập xong 1 dòng ấn Enter.\nVí dụ ma trận 4x4 đơn giản:\n0 1 0 1   hoặc   0101\n  0 1 0           010\n    0 1            01\n      0             0\n","_"*20)
    while True:
        if len(matrixMain) == len(matrixHeader):
            break
        matrixRaw = input(spaceInf)
        myMatrix = matrixRaw.strip().split(" ")
        if len(myMatrix) == 1:
            myMatrix = [i for i in myMatrix[0]]
        else:
            spaceInf += " "

        r = compile("^[01]")
        myMatrix = list(filter(r.match, myMatrix))

        if myMatrix[0] == '' or int(myMatrix[0]) != 0 or len(myMatrix) != (len(matrixHeader) - len(matrixMain)):
            print("Sai định dạng, vui lòng nhập lại!")
            printInputedMatrix(matrixMain)
        else:
            matrixMain.append(myMatrix)
            spaceInf += " "
    formatGr(matrixMain, matrixHeader, matrixMain + [])

def printInputedMatrix(matrixMain):
    blankString = ""
    for c in range(len(matrixMain)):
        print(blankString, end = "")
        for i in range(len(matrixMain[c])):
            print(matrixMain[c][i], end = " ")
        print("")
        blankString += "  "

def formatGr(matrixInput, matrixHeader, fullMatrix):
    browser = 0
    outputMatrix = []
    while True:
        if browser == len(matrixInput):
            break
        tempArr = []
        var = {
            "b": browser,
            "loop": 0
        }
        while var['b'] > 0:
            tempArr.append(matrixInput[var['loop']][var['b']])
            var['b'] -= 1
            var['loop'] += 1
        fullMatrix[browser] = tempArr + matrixInput[browser]
        browser += 1
    for i in range(0, len(fullMatrix)): 
        for j in range(0, len(fullMatrix[i])): 
            fullMatrix[i][j] = int(fullMatrix[i][j])
    startProgressMyWay(fullMatrix, matrixHeader)

def startProgressMyWay(mainArray, mainHeader):
    result = []

    if grMyWay(mainArray, mainHeader, result, 0, 0) == False:
        return False

    finishGr(result)

def grMyWay(mainArray, mainHeader, result, index, defaultColor):
    if (index == len(mainHeader)):
        return True

    if checkIt(mainArray, index, result, defaultColor, mainHeader) == True:
        result.append({"name": mainHeader[index], "color": defaultColor})
        grMyWay(mainArray, mainHeader, result, index+1, 0)
    else:
        grMyWay(mainArray, mainHeader, result, index, defaultColor+1)

def checkIt(mainArray, index, color, defaultColor, mainHeader):
    for c in range(index):
        if mainArray[c][index] == 1 and color[c]["color"] == defaultColor:
            return False
    return True

def finishGr(inputArray):
    groups = groupby(sorted(inputArray, key=lambda a: a["color"]), lambda a: a["color"])
    for key, group in groups:
        print("Color ID: %s, List: %s" % (key, ", ".join([i["name"] for i in list(group)])))

def main():
    initGr()
    quit(0)

if __name__ == "__main__":
  main()
