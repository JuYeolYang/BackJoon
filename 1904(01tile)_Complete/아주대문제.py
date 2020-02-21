#민솔이가 내준 아주대 문제 입니다.

import random

number_dic={}
number_list = []
key_string =""
irange = random.randint(1, 20)
for i in range(irange):
    number = random.randint(1, 9)
    number_list += "%d" % number
    key_string += "%d" % number

for key in number_list:
    if key not in number_dic:
        number_dic[key] = 1
    else: number_dic[key] += 1


result_dic_string = ""
for i in number_dic:
    result_dic_string += "(%s, %d)"%(i, number_dic[i])
print(key_string, "==", result_dic_string)