## Lê Song Vĩ
## MSSV: 1811061712
## Thuật giải tối ưu và tham lam

from itertools import groupby
from re import match, compile

a = ''
b = True
c = input
d = ' '
e = print
f = range
g = len

def grit():
    mspc = a
    matrixM = []
    whileLoop = 0
    while b:
        matrixH = c(
            "Hãy nhập đỉnh của ma trận cách nhau bằng khoảng trống (phím space). Nhập xong nhấn Enter\n"
            ).strip().split(d)
        if g(matrixH) == 1: matrixH = [i for i in matrixH[0]] if g(matrixH[0]) > 1 else []
        

        if g(matrixH) < 1:
            e("Đỉnh không hợp lệ")
        else:
            break;
    e(
        "Hãy nhập tam giác ma trận của bạn, nhập xong 1 dòng ấn Enter.\nVí dụ ma trận 4x4 đơn giản:\n0 1 0 1   hoặc   0101\n  0 1 0           010\n    0 1            01\n      0             0\n","_"*20)
    while b:
        if g(matrixM) == g(matrixH):
            break

        matrixR = c(mspc)
        imatrix = matrixR.strip().split(d)

        if g(imatrix) == 1:
            imatrix = [i for i in imatrix[0]]
        else:
            mspc += d

        r = compile("^[01]")
        imatrix = list(filter(r.match, imatrix))

        if imatrix[0] == a or int(imatrix[0]) != 0 or g(imatrix) != (g(matrixH) - g(matrixM)):
            e("Sai định dạng, vui lòng nhập lại!")
            rewmatrix(matrixM)
        else:
            matrixM.append(imatrix)
            mspc += d
    grformat(matrixM, matrixH, matrixM + [])

def rewmatrix(matrixM):
    tstr = a
    for c in f(g(matrixM)):
        e(tstr, end = a)
        for i in f(g(matrixM[c])):
            e(matrixM[c][i], end = d)
        e(a)
        tstr += d*2

def grformat(matrixI, matrixH, matrixF):
    brw = 0
    while b:
        if brw == g(matrixI):
            break
        tma = []
        var = {"a": brw, "b": 0}
        while var['a'] > 0:
            tma.append(matrixI[var['b']][var['a']])
            var['a'] -= 1
            var['b'] += 1
        matrixF[brw] = tma + matrixI[brw]
        brw += 1

    for i in f(0, g(matrixF)): 
        for j in f(0, g(matrixF[i])): 
            matrixF[i][j] = int(matrixF[i][j])

    start1(matrixF, matrixH); start2(matrixF, matrixH)

def start2(matrixMA, mainH):
    lareslt = []
    torder = gtorder(matrixMA)

    if gotize(matrixMA, mainH, lareslt, torder, [0]*g(mainH), [[] for i in f(g(mainH))]) == False:
        return False

    e("Tối ưu"); grfn(lareslt)

def gtorder(matrixMA):
    torder = [0]*g(matrixMA)
    for i in f(g(matrixMA)):
        for j in f(g(matrixMA[i])):
            torder[i] += matrixMA[i][j]

    return torder

def fcls(clist, cl, mainH):
    if g(cl) == 0:
        return 0

    for j in f(g(clist)):
        clist[j] = j
        for i in f(g(cl)):
            if clist[j] == cl[i]:
                break
            if i == g(cl) - 1:
                return clist[j]

    return 0

def gotize(matrixMA, mainH, lareslt, torder, clist, flist):
    if g(torder) == 0:
        return True
    mindex = max(f(g(torder)), key=torder.__getitem__)
    cl = fcls(clist, flist[mindex], mainH)
    lareslt.append({"property1": mainH[mindex], "property2": cl})

    deorder(matrixMA, mindex, torder, flist, cl)

    del mainH[mindex]; del torder[mindex]; del flist[mindex]
    refi(matrixMA, mindex)

    gotize(matrixMA, mainH, lareslt, torder, clist, flist)

def refi(matrixMA, idx):
    del matrixMA[idx]
    for i in f(g(matrixMA)):
        del matrixMA[i][idx]

def deorder(matrixMA, mindex, torder, flist, cl):
    for i in f(g(matrixMA[mindex])):
        if matrixMA[mindex][i] == 1:
            if torder[i] > 0:
                torder[i] -= 1
            flist[i].append(cl)

def start1(matrixMA, mainH):
    lareslt = []

    if grmway(matrixMA, mainH, lareslt, 0, 0) == False:
        return False

    e("Tham lam"); grfn(lareslt)

def grmway(matrixMA, mainH, lareslt, idx, dcolor):
    if (idx == g(mainH)):
        return True

    if chckt(matrixMA, idx, lareslt, dcolor, mainH) == True:
        lareslt.append({"property1": mainH[idx], "property2": dcolor})
        grmway(matrixMA, mainH, lareslt, idx+1, 0)
    else: grmway(matrixMA, mainH, lareslt, idx, dcolor+1)

def chckt(matrixMA, idx, cl, dcolor, mainH):
    for c in f(idx):
        if matrixMA[c][idx] == 1 and cl[c]["property2"] == dcolor:
            return False
    return True

def grfn(iarr):
    groups = groupby(sorted(iarr, key=lambda a: a["property2"]), lambda a: a["property2"])
    for key, group in groups: e("Mã màu: %s, Danh sách: %s" % (key, ", ".join([i["property1"] for i in list(group)])))

def main():
    grit()
    quit(0)

if __name__ == "__main__":
  main()
