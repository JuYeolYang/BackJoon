#���� 14501�� ��� ���� �Դϴ�.

N = int(input())
#T = ��� ��¥, P = ������� �� �޴� ��
T = list()
P = list()
#��� ��¥�� ���߱����� N+1�� ũ�⸸ŭ ����Ʈ �迭 ����
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
        Next_Counsel = day + T[day] - 1 #T[1] = 2, 1 + 2 = 3, 2��°�� ��ħ -> 3��°�� ���� �Ѵ�.
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
