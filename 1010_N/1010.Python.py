def facto(n):
    a = 1
    for i in range(n):
        a = a * (i + 1)
    return (a)

T = int(input(""))
end = 0
while (end != T):
    n ,m = map(int, int(input().split(' ')))

    e_r = facto(m)
    d_r = facto(n)
    d_s_r = facto(m-n)

    print(e_r//d_r//d_s_r)
    end += 1
