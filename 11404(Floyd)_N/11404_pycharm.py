#���� ���� 11404�� �÷��̵� �����Դϴ�.

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
������ �����ϴ� ������ i������ �´��� Ȯ���Ѵ�.
������ �����ϴ� ������ Ȯ���Ѵ�.
�����ϴ� �������� Ż �� �ִ� ������ �ٽ� ���캻��.
'''
for city in range(1, N + 1):
    for bus_number in range(1, M + 1):
        if city == bus_number:
            list_stop += bus[bus_number][1]
            list_bus += bus_number
