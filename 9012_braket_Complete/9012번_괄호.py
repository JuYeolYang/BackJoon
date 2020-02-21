n=int(input())
arr=[]
for i in range(n):
    arr.append(list(input()))
    if (arr[i][0] =='(' and arr[i][-1] ==')' and arr[i].count('(')==arr[i].count(')')):
        for j in range(len(arr[i])+1):
            if (arr[i][:j].count('(')<arr[i][:j].count(')')):
                print("NO")
                break
            else:
                print("YES")
                break
    else:
        print("NO")
