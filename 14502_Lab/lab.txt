#BackJoon No.14502
import random
import os
from time import sleep

N = int(input("N(행, 열) = "))

#Lab[y][x] : 행은 y값, 열은 x값이다.
Lab = [[1] * (N + 2) for x in range(N + 2)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        Lab[a][b] = random.randint(0,1)

x = random.randint(1, N)
y = random.randint(1, N)
Lab[y][x] = 2

#virus_point : 바이러스가 어디로 퍼졌는지 기록하는 리스트
#virus_count : x,y에 있는 바이러스가 4방향중 몇개의 방향으로 퍼졌는지 기록하는 리스트
virus_point = list()
virus_count = list()

def virus(x, y):
    count = 0
    #virus_subpoint : x,y에서 어디로 퍼졌는지 기록하는 리스트
    virus_subpoint = list()
    if Lab[y][x + 1] == 0:
        Lab[y][x + 1] = 2
        virus_subpoint.append([x + 1, y])
        count += 1
    if Lab[y][x - 1] == 0:
        Lab[y][x - 1] = 2
        virus_subpoint.append([x - 1, y])
        count += 1
    if Lab[y + 1][x] == 0:
        Lab[y + 1][x] = 2
        virus_subpoint.append([x, y + 1])
        count += 1
    if Lab[y - 1][x] == 0:
        Lab[y - 1][x] = 2
        virus_subpoint.append([x, y - 1])
        count += 1
    virus_point.append(virus_subpoint)
    virus_count.append(count)

virus(x, y)
start = 0
stop = len(virus_count)

while True:
    #새로 추가된 개수를 받는다.
    n = stop - start
    if n == 0:
        break

    for a in range(start, stop):
        count_v = virus_count[a]
        for b in range(count_v):
            x = virus_point[a][b][0]
            y = virus_point[a][b][1]
            virus(x, y)

    os.system('cls')

    for line in range(1, N + 1):
        str1 = ""
        for row in range(1, N + 1):
            str1 += str(Lab[line][row]) + " "
        print(str1)

    sleep(1)

    start = stop
    stop = len(virus_count)

save_room = 0
for line in range(1, N + 1):
    for row in range(1, N + 1):
        if Lab[line][row] == 0:
            save_room += 1
        
print("save_room : %d"%(save_room))