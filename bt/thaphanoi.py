## Lê Song Vĩ
## MSSV: 1811061712
## Giải bài toán tháp Hà Nội bằng phương pháp A*
## Backup: https://textvn.com/code/jz4zkcac

K = list
J = enumerate
D = len
import heapq as B
import copy


def A():
    print '''   |       |       |
   |       |       |
   |       |       |
___|___ ___|___ ___|___'''
    A = 2
    while A % 2 == 0 or A < 3:
        A = \
            int(input('Hãy nhập số đĩa của tháp: '
                ))
        if A % 2 == 0:
            print 'Vui lòng chỉ nhập số lẻ!'
        elif A < 3:
            print 'Số đĩa phải lớn hơn 3!'
    B = [[], [], []]
    D = [[], [], []]
    E(A, B, D)


def E(naNoiTower, initialGame, targetGame):
    B = targetGame
    A = initialGame
    for D in range(naNoiTower, 0, -1):
        A[0].append(D)
        B[2].append(D)
    E = F(A, B)
    print E


def H(linput):
    B = linput
    E = []
    for (G, C) in J(B):
        if C:
            F = C[-1]
            for (H, A) in J(B):
                if A is not C and (A and A[-1] > F or not A):
                    D = copy.deepcopy(B)
                    D[G].pop()
                    D[H].append(F)
                    E.append(D)
    return E


class G(K):

    def cCalc(A):
        if D(A) > 0:
            B = A[-1]
            C = D(B[0])
            return D(A) - 1 + C
        else:
            return 0

    def __lt__(A, other):
        return A.cCalc() < other.cCalc()


def F(initList, targetList):
    C = K()
    I = G([initList])
    A = []
    B.heappush(A, I)
    while True:
        if not A:
            return False
        D = B.heappop(A)
        E = D[-1]
        C.append(E)
        if E == targetList:
            return D
        for F in H(E):
            if F not in C:
                J = G(D + [F])
                B.heappush(A, J)
                C.append(F)


def I():
    A()
    quit(0)


if __name__ == '__main__':
    I()
