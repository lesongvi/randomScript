## Lê Song Vĩ
## MSSV: 1811061712
## Thuật toán GTS1. Từ đó có thể suy ra GTS2
## Backup: https://textvn.com/code/ft4ezxen

M = list
G = input
J = True
F = print
A = len
from sys import maxsize as I


def C():
    L = " "
    H = ""
    D = []
    N = 0
    while J:
        B = (
            G(
                "Hãy nhập đỉnh của ma trận cách nhau bằng khoảng trống (phím space). Nhập xong nhấn Enter\n"
            )
            .strip()
            .split(L)
        )
        if A(B) == 1:
            B = [A for A in B[0]] if A(B[0]) > 1 else []
        if A(B) < 1:
            F("Đỉnh không hợp lệ")
        else:
            break
    F("Hãy nhập ma trận, nhập xong 1 dòng ấn Enter.\n", "_" * 20)
    while J:
        if A(D) == A(B):
            break
        I = G(H)
        C = I.strip().split(L)
        if A(C) == 1:
            C = [A for A in C[0]]
        K = compile("^[01]")
        C = M(filter(K.match, C))
        if A(C) == A(B):
            D.append(C)
    E(B, startHeader, D, [])


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


def E(matrixHeader, startHeader, matrixMain, flist):
    G = matrixMain
    C = startHeader
    B = matrixHeader
    N = C
    H = [C]
    D = 0
    I = B.index(C)
    K = 0
    while J:
        if K == A(B) - 1:
            break
        E = L(I, G, flist, B)
        H.append(B[E])
        D = G[I][E]
        F(D)
        I = E
        K = 1
    H.append(C)
    D = G[E][B.index(C)]
    F(" -> ".join([str(A) for A in M(H)]), "=", D)


def B():
    B = [
        [0, 20, 42, 31, 6, 24],
        [10, 0, 17, 6, 35, 18],
        [25, 5, 0, 27, 14, 9],
        [12, 9, 24, 0, 30, 12],
        [14, 7, 21, 15, 0, 38],
        [40, 15, 16, 5, 20, 0],
    ]
    C = [1, 2, 3, 4, 5, 6]
    A = 4
    E(C, A, B, [A])
    quit(0)


if __name__ == "__main__":
    B()
