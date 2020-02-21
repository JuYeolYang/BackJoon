#백준 14501번 퇴사 문제 입니다.

N = int(input())
#T = 상담 날짜, P = 상담했을 때 받는 돈
T = list()
P = list()
#상담 날짜랑 맞추기위해 N+1의 크기만큼 리스트 배열 생성
T = [0]
P = [0]

#print(day)

for count in range(1, N + 1):
    inputs = input()
    a, b = map(int, inputs.split())
    T.append(a)
    P.append(b)

print(T)
print(P)

def solve(day):
    if day <= N:
        Next_Counsel = day + T[day] - 1 #T[1] = 2, 1 + 2 = 3, 2일째에 마침 -> 3일째로 들어가야 한다.
        if Next_Counsel == N:
            return P[day]
        if Next_Counsel > N:
            return 0
        if Next_Counsel < N:
            max_solve = 0
            for a in range(Next_Counsel + 1, N + 1):
                if max_solve < solve(a):
                    max_solve = solve(a)
            return P[day] + max_solve
    else:
        return 0

max_pay = 0

for section in range(1, T[1] + 1):
    if max_pay < solve(section):
        max_pay = solve(section)

print(max_pay)
