import random

def find_yes_or_not(n):
    arr=[]
    for i in range(n):
        for j in random.randrange(2,51):
            if random.randrange(2)==1:
                arr[i].append('(')
            else: arr[i].append(')')
    for i in range(n):
        if arr[i].count('(')==arr[i].count(')'):
            print("Yes")
        else: print("No")

num=int(input("문자열 개수"))
find_yes_or_not(num)
