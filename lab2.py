import random
n1 = int(input())
str1 = list(map(int, input().split()))
n2 = int(input())
str2 = list(map(int, input().split()))


def quick(str):
    if len(str) <= 1:
        return str
    else:
        k = random.choice(str)
        bolshe = []
        menshe = []
        ravnoe = []
        for t in str:
            if t < k:
                menshe.append(t)
            elif t > k:
                bolshe.append(t)
            else:
                ravnoe.append(t)
        return quick(menshe) + ravnoe + quick(bolshe)
sort1 = quick(str1)
sort2 = quick(str2)
if n2 >= n1:
    for a in range(n1):
        if sort2[a] == sort1[a]:
            sort2 = list(filter((a).__ne__, sort2))
            sort1 = list(filter((a).__ne__, sort1))
            print(sort2)
    if sort2 ==[]:
        print('da')
    else:
        print('no')
elif n1 > n2:
    for a in range(n2):
        if sort1[a] == sort2[a]:
            sort1 = list(filter((a).__ne__, sort1))
            sort2 = list(filter((a).__ne__, sort2))
    if sort1 ==[]:
        print('da')
    else:
        print('no')