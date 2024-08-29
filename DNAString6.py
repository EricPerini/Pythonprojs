string1 = input('DNA 1: ')
string2 = input('DNA 2: ')
a = 0
L1 = list(string1)
L2 = list(string2)


for i in range(len(L1)):
    if L1[i]==L2[i]:
        continue
    else:
        a+=1

print(a)