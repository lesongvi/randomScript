## Lê Song Vĩ
## MSSV: 1811061712
## Giải trò chơi Taci bằng phương pháp AKT
## Backup: https://textvn.com/code/evx58hr3

#!/usr/bin/python
# -*- coding: utf-8 -*-
V = int
U = input
N = 'g'
I = True
K = 'matrix'
J = 'location'
H = sorted
F = 'h'
E = 'f'
C = range
A = len
import pickle as G


def B():
    L = \
        'Sai định dạng, vui lòng nhập đúng định dạng'
    K = ' '
    J = '_'
    H = '\n'
    C = []
    E = []
    G = \
        '''- Ví dụ ma trận hợp lệ:
1 0 7   hoặc   107
5 4 8   hoặc   548
2 3 6   hoặc   236'''
    print 'Quy ước: số 0 trong ma trận là khoảng trống.'
    print ('Hãy nhập ma trận ban đầu, nhập xong 1 dòng ấn Enter'
           , G, H, J * 20)
    while I:
        if A(C) != 0 and A(C) == A(C[0]):
            break
        F = U()
        B = F.strip().split(K)
        if A(B) == 1:
            B = [A for A in B[0]]
        if A(C) != 0 and A(B) != A(C[0]) or A(B) > 3:
            print L
        else:
            C.append(B)
    print ('Hãy nhập ma trận kết thúc, nhập xong 1 dòng ấn Enter'
           , G, H, J * 20)
    while I:
        if A(E) == A(C):
            break
        F = U()
        B = F.strip().split(K)
        if A(B) == 1:
            B = [A for A in B[0]]
        if A(B) != A(C):
            print L
        else:
            E.append(B)
    O(C, E)


def O(matrixMain, matrixTarget):
    G = matrixTarget
    B = matrixMain
    for D in C(A(B)):
        for H in C(A(B[D])):
            B[D][H] = V(B[D][H])
            G[D][H] = V(G[D][H])
    I = M(B, G)
    O = [{
        J: [],
        N: 0,
        E: I,
        F: I,
        K: B,
        }]
    L(
        B,
        G,
        1,
        I,
        I,
        [B],
        O,
        )


def L(
    matrixInput,
    targetMatrix,
    g,
    h,
    f,
    flist,
    process,
    ):
    C = flist
    B = targetMatrix
    A = process
    G = Q(matrixInput)
    P(G, B, C, A, g)
    if h != 0:
        del A[0]
        A = H(A, key=lambda x: x[F] and x[E])
        L(
            A[0][K],
            B,
            A[0][N] + 1,
            A[0][F],
            A[0][E],
            C,
            A,
            )
    else:
        print ('result: ', ' => '.join([B for B in A[0][J]]))


def R(list1, list2):
    for A in list1:
        if H(A) == H(list2):
            return False
    return I


def S(listInput):
    A = listInput
    if A == [0, 1]:
        return 'trái'
    elif A == [1, 0]:
        return 'lên'
    elif A == [-1, 0]:
        return 'xuống'
    elif A == [0, -1]:
        return 'phải'
    else:
        return None


def P(
    blankPosij,
    targetMatrix,
    flist,
    process,
    g,
    ):
    O = flist
    I = process
    B = blankPosij
    L = H(I, key=lambda x: x[F] and x[E])[0][K]
    T = H(I, key=lambda x: x[F] and x[E])[0][J]
    for C in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        if B[0] + C[0] < 0 or B[1] + C[1] < 0 or B[0] + C[0] > A(L) - 1 \
            or B[1] + C[1] > A(L) - 1:
        else:
            D = G.loads(G.dumps(L, -1))
            P = G.loads(G.dumps(T, -1))
            D[B[0]][B[1]] = D[B[0] + C[0]][B[1] + C[1]]
            D[B[0] + C[0]][B[1] + C[1]] = 0
            if R(O, D):
                O.append(D)
                Q = M(D, targetMatrix)
                P.append('%s %s' % (D[B[0]][B[1]], S(C)))
                I.append({
                    J: P,
                    N: g,
                    E: g + Q,
                    F: Q,
                    K: D,
                    })


def Q(matrixInput):
    B = matrixInput
    for D in C(A(B)):
        for E in C(A(B)):
            if B[D][E] == 0:
                return [D, E]


def M(matrixInput, targetMatrix):
    F = targetMatrix
    B = matrixInput
    G = 0
    for D in C(A(B)):
        for E in C(A(F)):
            if B[D][E] != F[D][E] and B[D][E] != 0:
                G += 1
    return G


def T():
    B()
    quit(0)


if __name__ == '__main__':
    T()
