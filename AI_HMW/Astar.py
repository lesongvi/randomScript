## Lê Song Vĩ
## MSSV: 1811061712
## Thuật toán A sao
## Backup: https://textvn.com/astar

R = True
Q = False
P = input
O = max
L = print
C = range
B = enumerate
A = len
import copy
import heapq as D
import sys


class E:

    def __init__(A, copyFrom=None):
        B = copyFrom
        if B:
            A.rods = copy.deepcopy(B.rods)
        else:
            A.rods = [[], [], []]

    def numDisksInRod(B, rodNum):
        return A(B.rods[rodNum])

    def nextStates(C):
        G = []
        for (I, D) in B(C.rods):
            if D:
                H = D[-1]
                for (J, A) in B(C.rods):
                    if A is not D and (A and A[-1] > H or not A):
                        F = E(C)
                        F.rods[I].pop()
                        F.rods[J].append(H)
                        G.append(F)
        return G

    def addDiskToRod(A, diskNum, rodNum):
        C = rodNum
        B = diskNum
        assert B > 0
        assert C >= 0 and C <= 3
        L(A.rods)
        assert A.rods and A.rods[-1] > B or not A.rods
        A.rods[C].append(B)

    def __eq__(A, other):
        for (C, D) in B(A.rods):
            if D != other.rods[C]:
                return Q
        return R

    def maxDiskSize(A):
        return O(O(A.rods))

    def __hash__(A):
        hash = 0
        D = A.maxDiskSize()
        for (E, F) in B(A.rods):
            C = 0
            for G in F:
                C += 1 << G - 1
            hash += C << D * E
        return hash

    def __repr__(E):
        Q = '\n'
        F = E.maxDiskSize()
        K = F * 2 + 1
        L = 2
        G = A(E.rods)
        R = K * G + (G - 1) * L
        H = F
        I = [[' '] * R for A in C(H)]
        for M in C(G):
            D = M * (K + L) + H
            for J in C(H):
                I[J][D] = '|'
            for (S, N) in B(E.rods[M]):
                T = F - 1 - S
                for O in C(D - N, D + N + 1):
                    if O != D:
                        I[T][O] = '_'
        P = Q
        for J in I:
            P += ''.join(J) + Q
        return P + Q


class G(list):

    def cost(B):
        if A(B) > 0:
            C = B[-1]
            D = C.numDisksInRod(0)
            return A(B) - 1 + D
        else:
            return 0

    def __lt__(A, other):
        return A.cost() < other.cost()


def M(initialState, goal):
    B = set()
    H = G([initialState])
    A = []
    D.heappush(A, H)
    while R:
        if not A:
            return Q
        C = D.heappop(A)
        E = C[-1]
        B.add(E)
        if E == goal:
            return C
        for F in E.nextStates():
            if F not in B:
                I = G(C + [F])
                D.heappush(A, I)
                B.add(F)


F = E()
H = E()
I = \
    int(P('Nhập số đĩa (phải lớn hơn 0): '
        ))
if I <= 0:
    sys.exit('Số đĩa phải lớn hơn 0'
             )
for J in C(I, 0, -1):
    F.addDiskToRod(J, 0)
    H.addDiskToRod(J, 2)
K = M(F, H)
L('Đường đi tối ưu nhất là đi %s bước'
   % (A(K) - 1))
N = \
    P('Bạn có muốn xem các bước được thực hiện của đường tối ưu (Y/N)?  '
      )
if N.lower()[0] == 'y':
    L(K)
