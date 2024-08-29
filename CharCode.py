def RandCode():
    import random
    Alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    k = 0
    code = []
    for i in range(15):
        k = random.randint(0, 1)
        if k==0:
            x = random.randint(0, 25)
            code.append(Alfabeto[x])
        elif k==1:
            x = random.randint(0, 9)
            code.append(x)
    word = ''.join(str(i) for i in code)
    return word

def PrivateCode(a):
    k = a
    k1 = []
    result = 1
    for  i in range(15):
        if k[i].isnumeric():
            if k[i]=='0':
                continue
            else:
                k1.append(k[i])
    lenk1 = len(k1)
    for i in range(lenk1):
        result = result*int(k1[i])
    word = ''.join(str(i)for i in k1) + str(result) + '-' + str(lenk1)
    return word

def KeyChecker(a, b):
    Code = a
    Key = b
    Codelist = list(Code)
    KeyDiv = Key.split('-')
    lenk1 = int(KeyDiv[1])
    KeyList = list(KeyDiv[0])
    Numbers = KeyList[:lenk1]
    Multi = int(''.join(str(i)for i in KeyList[lenk1:]))
    result = Multi
    k1= []
    for  i in range(len(Codelist)):
        if Codelist[i].isnumeric():
            if Codelist[i]=='0':
                continue
            else:
                k1.append(Codelist[i])
    if len(Numbers)==len(k1):
        for i in range(len(Numbers)):
            result = result/int(k1[i])
        if result==1:
            return True
        else:
            return False
    else:
        return False