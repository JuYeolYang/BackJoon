#백준 1904번 : 01타일
import math
#N의 값을 받는다
N = int(input())

result = []
for i in range(N + 1):
    result += [0]
result[1] = 1
result[2] = 2

for i in range(3,N + 1):
    result[i] = result[i - 1] + result[i - 2]
    #int 범위를 벗어 나기 때문에 15746을 미리 나눠 준다.
    result[i] %= 15746

print(result[N])


'''
import math
#N의 값을 받는다
N = int(input())
result = []

#문제에서 0 또는 1이 총 N개가 들어가기 때문에 풀기 쉽도록 N + 1개의 배열을 할당한다.
for i in range(N + 1):
    result += [0]

count = 0
#result를 비트로 계산하는 목적이다.
#그러므로 result는 [0,...,0]부터 [1,...,1]까지를 구하기 위해서는 일단 result[1]을 -1로 해준다.
result[1] = -1

#각 항마다 0또는 1이 들어갈 경우는 2가지 이다. 따라서 크기가 N인 배열이 가지는 경우의 수는 2의 N승 가지 수 이다.
for number_of_case in range(1, 2**N + 1):
    #result 리스트가 맞는지 검사하기 위해 Iscorrect를 도입한다.
    Iscorrect = True
    result[1] += 1

    for calculate_bits in range(1, N + 1):
        # i 행이 2이이면 i행에 0을 대입하고 i+1행에 1을 더해준다.
        if result[calculate_bits] == 2:
            result[calculate_bits + 1] += 1
            result[calculate_bits] = 0
    #print(result)
    check_each_section = 1
    while check_each_section <= N:
        if result[check_each_section] == 0:
            #k항이 N항과 동일하면 K+1항은 존재하지 않으므로 Iscorrect에 False값을 반환한다.
            if check_each_section == N:
                Iscorrect = False
                break
            if result[check_each_section + 1] == 0:
                #k+1항이 0인것을 확인했으면 k+1을 확인 할 필요가 없으므로 k+1항을 건너뛴다.
                check_each_section += 2
                continue
            else:
                Iscorrect = False
                break
        check_each_section += 1

    if Iscorrect:
        count += 1

print(round(count%15746))
'''

'''
N = 1:
    (1) - 1개
N = 2:
    (0,0) , (1,1) - 2개
N = 3:
    (0,0,1), (1,0,0) , (1,1,1) - 3개
    0,0 - N(1), 1, - N(2)
N = 4:
    (0,0,0,0), (1,0,0,1), (0,0,1,1), (1,1,0,0), (1,1,1,1) - 5개
    0,0 - N(2), 1, - N(3) 
'''
