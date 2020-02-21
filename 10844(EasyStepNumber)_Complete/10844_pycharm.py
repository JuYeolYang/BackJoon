N = int(input())

num_arr = []
for line in range(N + 1):
    #N+1개만큼 배열을 만든다.
    num_arr += [[0] * 11]

for number in range(10):
    #1로 초기화 한다.
    num_arr[1][number] = 1

for line in range(2, N + 1):
    for number in range(1, 10):
        #ex) N = 3(처음숫자 : 2) N = 2일때의 처음 숫자 1일때와 0일때의 경우의 수를 더한 값과 같다.
        num_arr[line][number] = num_arr[line - 1][number - 1] + num_arr[line - 1][number + 1]
        num_arr[line][0] = num_arr[line - 1][1]

result = 0
for N_number in range(1, 10):
    result += num_arr[N][N_number]
    result %= 1000000000

print(result)
