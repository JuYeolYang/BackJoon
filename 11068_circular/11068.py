#Circular Problem

N = int(input())

def Circular(n):
    number = n
    if n < 0:
        return 0
    else:
        count = 0
        while True:
                if (number % (10**count)) != number:
                    count += 1
                else: break
        #print(count)
        while number != 0:
            if (number % 10) == (number // 10 ** (count - 1)):    #n번째 자릿수와 첫번째 자리수가 같은지 확인함
                number = (number % (10 ** (count - 1))) // 10   #같으면 10의 n승으로 나눈 나머지를 10으로 나눈 몫으로 반환
                #print(number)
                count -= 2
                if count == 1:
                    return 1
            else: return 0


for a in range(N):
    input_number = int(input())
    print(Circular(input_number))