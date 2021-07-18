## Lê Song Vĩ
## MSSV: 1811061712
## Thuật toán GTS1. Từ đó có thể suy ra GTS2
## Backup: https://textvn.com/code/h6cfkurx

J = input
F = str
G = True
E = list
B = print
A = len
from sys import maxsize as I
import copy, random, math


def K():
    M = " "
    I = ""
    F = []
    N = 0
    while G:
        C = (
            J(
                "Hãy nhập đỉnh của ma trận cách nhau bằng khoảng trống (phím space). Nhập xong nhấn Enter\n"
            )
            .strip()
            .split(M)
        )
        if A(C) == 1:
            C = [A for A in C[0]] if A(C[0]) > 1 else []
        if A(C) < 1:
            B("Đỉnh không hợp lệ")
        else:
            break
    B("Hãy nhập ma trận, nhập xong 1 dòng ấn Enter.\n", "_" * 20)
    while G:
        if A(F) == A(C):
            break
        K = J(I)
        D = K.strip().split(M)
        if A(D) == 1:
            D = [A for A in D[0]]
        L = compile("^[01]")
        D = E(filter(L.match, D))
        if A(D) == A(C):
            F.append(D)
    H(C, startHeader, F, [])


def L(currentPoint, matrixMain, flist, mHeader):
    G = flist
    F = matrixMain
    E = mHeader
    D = currentPoint
    H = I
    C = -1
    for B in range(A(E)):
        if D != B and E[B] not in G:
            if F[D][B] < H:
                H = F[D][B]
                C = B
    if C != -1:
        G.append(E[C])
    return C


def H(matrixHeader, startHeader, matrixMain, flist):
    E = matrixMain
    C = startHeader
    B = matrixHeader
    M = C
    H = [C]
    I = 0
    F = B.index(C)
    K = 0
    J = []
    while G:
        if K == A(B) - 1:
            break
        D = L(F, E, flist, B)
        H.append(B[D])
        I = E[F][D]
        J.append(E[F][D])
        F = D
        K = 1
    H.append(C)
    I = E[D][B.index(C)]
    J.append(E[D][B.index(C)])
    return [I, H, J]


def C(matrixHeader, matrixMain, pNum):
    K = " -> "
    D = math.inf
    C = [2, 3, 5, 6]
    B("p =", pNum, ", V =", C)
    I = []
    J = 0
    while G:
        if J == pNum:
            break
        J = 1
        B("GTS1(%d)" % C[0])
        A = H(matrixHeader, C[0], matrixMain, [C[0]])
        B("T = ", K.join([F(B) for B in E(A[1])]))
        B("C =", "   ".join([F(B) for B in E(A[2])]), " = ", A[0])
        if A[0] < D:
            B("C < BestCost => BestCost = C")
            D = A[0]
            I = A[1]
        else:
            B("C > BestCost")
        del C[0]
    B(K.join([F(A) for A in E(I)]), "=", D)


def D():
    A = [
        [0, 20, 42, 31, 6, 24],
        [10, 0, 17, 6, 35, 18],
        [25, 5, 0, 27, 14, 9],
        [12, 9, 24, 0, 30, 12],
        [14, 7, 21, 15, 0, 38],
        [40, 15, 16, 5, 20, 0],
    ]
    B = [1, 2, 3, 4, 5, 6]
    E = 6
    D = 4
    C(B, A, D)
    quit(0)


if __name__ == "__main__":
    D()
