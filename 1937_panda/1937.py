# 1937백준 문제

import random

N = int(input("정사각형크기: "))
test = int(input("테스트 횟수: "))

# bamboo : 대나무 개수, life : 정해진 위치에서 가장 오래 살아 남을 수 있는 일수
bamboo = [[0] * (N + 2) for x in range(N + 2)]
life = [[0] * (N + 2) for x in range(N + 2)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        bamboo[i][j] = random.randint(1, 20)

# 생존일 계산
def life_time(x, y):
    # 현위치
    now = bamboo[y][x]

    # 4방향에서 대나무 개수가 현위치보다 적으면 현위치에서는 하루밖에 살 수 없다.
    if now >= bamboo[y + 1][x] and now >= bamboo[y - 1][x] and now >= bamboo[y][x + 1] and now >= bamboo[y][x - 1]:
        life[y][x] = 1
        return 1

    # 북쪽방향에 대나무가 많은 경우
    if now < bamboo[y + 1][x]:
        # 현위치에 동서남북 위치의 대나무 개수를 비교를 한다.
        # 어느 위치로 움직여야 더 오래 살수 있을 지 모르므로 움직인 위치의 생존일 수를 대입하고
        # 다른 쪽으로 움직였을 때 생존일수를 비교하여 더 큰 곳에 +1을 하여 대입한다.
        if life[y][x] < life_time(x, y + 1) + 1:
            life[y][x] = life_time(x, y + 1) + 1 

    # 남쪽방향에 대나무가 많은 경우
    if now < bamboo[y - 1][x]:
        if life[y][x] < life_time(x, y - 1) + 1:
            life[y][x] = life_time(x, y - 1) + 1

    # 동쪽방향에 대나무가 많은 경우
    if now < bamboo[y][x + 1]:
        if life[y][x] < life_time(x + 1, y) + 1:
            life[y][x] = life_time(x + 1, y) + 1

    # 서쪽방향에 대나무가 많은 경우
    if now < bamboo[y][x - 1]:
        if life[y][x] < life_time(x - 1, y) + 1:
            life[y][x] = life_time(x - 1, y) + 1
    
    return life[y][x]


for t in range(test):
    # 위치마다 대나무 개수 출력
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            bamboo[i][j] = random.randint(1, 20)

    # 임의의 초기위치 설정
    point_x = random.randint(1, N)
    point_y = random.randint(1, N)

    # 대나무 개수 확인
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print("%3d"%(bamboo[i][j]), end = " ")
        print("")
    print("")
    
    # 판다 위치 확인
    print("x = %d, y = %d"%(point_x, point_y))

    # 판다 최대생존 일수 출력
    print("최장생존: ", life_time(point_x, point_y))
    print("")

    # 판다 움직인 경로 확인
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print("%3d"%(life[i][j]), end = " ")
        print("")
    print("")

    # 다음 테스트를 진행하기 위해서는 life리스트를 모두 0으로 초기화 시켜주어야 한다.
    life = [[0] * (N + 2) for x in range(N + 2)]

    