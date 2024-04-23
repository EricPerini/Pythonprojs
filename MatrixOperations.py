def MtrxMult():
    print('Matriz 1')
    LineQunt_m1 = int(input('Quantas linhas: '))
    ClumQunt_m1 = int(input('Quantas Colunas: '))
    print('Matriz 2')
    LineQunt_m2 = ClumQunt_m1
    ClumQunt_m2 = int(input('Quantas Colunas: '))
    print('Matriz 1')
    M1 = []
    M1_aux = []
    for i in range(LineQunt_m1):
        for j in range(ClumQunt_m1):
            x = float(input(f'Elemento da Linha {i+1} e coluna {j+1}: '))
            M1_aux.append(x)
        M1.append(M1_aux[:])
        M1_aux.clear()
    print('Matriz 2')
    M2 = []
    M2_aux = []
    for i in range(LineQunt_m2):
        for j in range(ClumQunt_m2):
            y = float(input(f'Elemento da Linha {i+1} e coluna {j+1}: '))
            M2_aux.append(y)
        M2.append(M2_aux[:])
        M2_aux.clear()
    MT = []
    for i in range(ClumQunt_m2):
        MT_aux = []
        for j in range(LineQunt_m2):
            MT_aux.append(0)
        MT.append(MT_aux[:])
    for i in range(LineQunt_m2):
        for j in range(ClumQunt_m2):
            MT[j][i] = M2[i][j]
    MR = []
    for j in range(LineQunt_m1):
        MR_aux = []
        for k in range(len(MT)):
            a1 = 0
            for l in range(len(M2)):
                x = float(M1[j][l])*float(MT[k][l])
                a1 = a1+x
            MR_aux.append(a1)
        MR.append(MR_aux[:])
    return MR[:]
    
def MtrxDet():
    LineQunt_m1 = int(input('Quantas linhas: '))
    ClumQunt_m1 = LineQunt_m1
    M1 = []
    M1_aux = []
    for i in range(LineQunt_m1):
        for j in range(ClumQunt_m1):
            x = float(input(f'Elemento da Linha {i+1} e coluna {j+1}: '))
            M1_aux.append(x)
        M1.append(M1_aux[:])
        M1_aux.clear()
    if LineQunt_m1<3:
        a = 1
        b = 1
        d = 0
        for i in range(LineQunt_m1):
            for j in range(ClumQunt_m1):
                if LineQunt_m1==1:
                    a = x
                    b = 0
                    break
                elif i==j:
                    a = a*M1[i][j]
                else:
                    b = b*M1[i][j]
        d = d+a-b
    elif LineQunt_m1==3:
        for i in range(LineQunt_m1):
            M2 = [0, 0]
            for j in range(ClumQunt_m1-1):
                M2[j] = M1[i][j]
            M1[i].extend(M2[:])
        a = 1
        b = 1
        c = 1
        d = 0
        k = 0
        for i in range(LineQunt_m1):
            for j in range(5):
                if i==j:
                    a = a*M1[i][j]
                elif j-i==1:
                    b = b*M1[i][j]
                elif j-i==2:
                    c = c*M1[i][j]
        d = d+a+b+c
        a = 1
        b = 1
        c = 1
        for i in range(LineQunt_m1):
            for j in range(5):
                k =k+1
                if (k==5) or (k==9) or (k==13):
                    a = a*M1[i][j-5]
                elif (k==4) or (k==8) or (k==12):
                    b = b*M1[i][j-5]
                elif (k==3) or (k==7) or (k==11):
                    c = c*M1[i][j-5]
        d = d-a-b-c
    return d

def MtrxCrt(x, y):
    MR = []
    for i in range(x):
        MR_aux = []
        for j in range(y):
            MR_aux.append(0)
        MR.append(MR_aux[:])
    return MR[:]

def MtrxSum():
    print('Matriz 1')
    LineQunt_m1 = int(input('Quantas linhas: '))
    ClumQunt_m1 = int(input('Quantas Colunas: '))
    print('Matriz 1')
    M1 = []
    M1_aux = []
    for i in range(LineQunt_m1):
        for j in range(ClumQunt_m1):
            x = int(input(f'Elemento da Linha {i+1} e coluna {j+1}: '))
            M1_aux.append(x)
        M1.append(M1_aux[:])
        M1_aux.clear()
    print('Matriz 2')
    M2 = []
    M2_aux = []
    for i in range(LineQunt_m1):
        for j in range(ClumQunt_m1):
            y = int(input(f'Elemento da Linha {i+1} e coluna {j+1}: '))
            M2_aux.append(y)
        M2.append(M2_aux[:])
        M2_aux.clear()
    MR = MtrxCrt(LineQunt_m1, ClumQunt_m1)
    for i in range(LineQunt_m1):
        for j in range(ClumQunt_m1):
            MR[i][j] = float(M1[i][j])+float(M2[i][j])
    return MR[:]

def MtrxSub():
    print('Matriz 1')
    LineQunt_m1 = int(input('Quantas linhas: '))
    ClumQunt_m1 = int(input('Quantas Colunas: '))
    print('Matriz 1')
    M1 = []
    M1_aux = []
    for i in range(LineQunt_m1):
        for j in range(ClumQunt_m1):
            x = int(input(f'Elemento da Linha {i+1} e coluna {j+1}: '))
            M1_aux.append(x)
        M1.append(M1_aux[:])
        M1_aux.clear()
    print('Matriz 2')
    M2 = []
    M2_aux = []
    for i in range(LineQunt_m1):
        for j in range(ClumQunt_m1):
            y = int(input(f'Elemento da Linha {i+1} e coluna {j+1}: '))
            M2_aux.append(y)
        M2.append(M2_aux[:])
        M2_aux.clear()
    MR = MtrxCrt(LineQunt_m1, ClumQunt_m1)
    for i in range(LineQunt_m1):
        for j in range(ClumQunt_m1):
            MR[i][j] = float(M1[i][j])-float(M2[i][j])
    return MR[:]