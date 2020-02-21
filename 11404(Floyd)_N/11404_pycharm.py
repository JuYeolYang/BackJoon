#백준 문제 11404번 플로이드 문제입니다.

N = int(input())
M = int(input())

cities = [[0]*N]*N
bus = []
list_start = []
list_stop = []
list_bus = []
for i in range(M + 1):
    bus += [[0,0,0]*i]

for bus_number in range(1, M + 1):
    bus[bus_number][0] = int(input())
    bus[bus_number][1] = int(input())
    bus[bus_number][2] = int(input())

'''
버스가 시작하는 지점이 i번줄이 맞는지 확인한다.
버스가 도착하는 지점을 확인한다.
도착하는 지점에서 탈 수 있는 버스를 다시 살펴본다.
'''
for city in range(1, N + 1):
    for bus_number in range(1, M + 1):
        if city == bus_number:
            list_stop += bus[bus_number][1]
            list_bus += bus_number
