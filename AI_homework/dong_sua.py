## Lê Song Vĩ
## MSSV: 1811061712
## Giải bài toán đong sữa
## Backup: https://textvn.com/dongSua

J = list
E = print
A = None
import heapq as C


class G:

    def __init__(A):
        A.capacities = (4, 3)

    def startState(A):
        return (0, 0)

    def isGoal(A, state):
        return state[0] == 2

    def getSuccessors(G, J1, J2):
        B = J2
        A = J1
        C = []
        (E, F) = G.capacities
        if A < E:
            C.append(((E, B), 'Đổ vào J1', 1))
        if B < F:
            C.append(((A, F), 'Đổ vào J2', 1))
        if A > 0:
            C.append(((0, B), 'Đổ ra J1', 1))
        if B > 0:
            C.append(((A, 0), 'Đổ ra J2', 1))
        if A + B <= 3:
            D = A + B
            C.append(((0, D), 'Đổ J1 vào J2',
                     1))
        if A + B <= 4:
            D = A + B
            C.append(((D, 0), 'Đổ J2 vào J1',
                     1))
        if A + B > 4:
            D = A + B - 4
            C.append(((E, D), 'Đổ J1 từ J2'
                     , 1))
        if A + B > 3:
            D = A + B - 3
            C.append(((D, F), 'Đổ J2 từ J1'
                     , 1))
        return C


def H(state, problem=A):
    return abs(state[0] - 2)


class F(J):

    def __init__(
        A,
        state,
        path,
        cost=0,
        heuristic=0,
        problem=A,
        ):
        A.state = state
        A.path = path
        A.cost = cost
        A.heuristic = heuristic
        A.problem = problem

    def getSuccessors(A, heuristicFunction=A):
        C = heuristicFunction
        D = []
        for B in A.problem.getSuccessors(A.state):
            E = B[0]
            G = J(A.path)
            G.append(B[1])
            I = A.cost + B[2]
            if C:
                H = C(E, A.problem)
            else:
                H = 0
            K = F(E, G, I, H, A.problem)
            D.append(K)
        return D


def B(state, problem=A):
    return 0


def D(problem, heuristic=B):
    D = problem
    G = set()
    A = F(D.startState(), [], 0, 0, D)
    C.heappush(A, A.cost + A.heuristic)
    H = 0
    while True:
        if len(A) == 0:
            return False
        B = C.heappop(A)
        H += 1
        if D.isGoal(B.state):
            return B.path
        if B.state not in G:
            G.add(B.state)
            for E in B.getSuccessors(heuristic):
                C.heappush(E, E.cost + E.heuristic)


def I():
    A = G()
    C = D(A, H)
    C = D(A, B)
    E(C)


I()
