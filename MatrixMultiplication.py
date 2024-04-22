print('Matriz 1')
LineQunt_m1 = int(input('Quantas linhas: '))
ClumQunt_m1 = int(input('Quantas Colunas: '))
print('Matriz 2')
LineQunt_m2 = ClumQunt_m1
ClumQunt_m2 = int(input('Quantas Colunas: '))


'Reading the Matrix'

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
for i in range(LineQunt_m2):
    for j in range(ClumQunt_m2):
        y = int(input(f'Elemento da Linha {i+1} e coluna {j+1}: '))
        M2_aux.append(y)
    M2.append(M2_aux[:])
    M2_aux.clear()


'Transposing the matrix'

MT = []
for i in range(ClumQunt_m2):
    MT_aux = []
    for j in range(LineQunt_m2):
        MT_aux.append(0)
    MT.append(MT_aux[:])

for i in range(LineQunt_m2):
    for j in range(ClumQunt_m2):
        MT[j][i] = M2[i][j]


'Multiplicating Both'

MR = []
for j in range(LineQunt_m1):
    MR_aux = []
    for k in range(len(MT)):
        a1 = 0
        for l in range(len(M2)):
            x = int(M1[j][l])*int(MT[k][l])
            a1 = a1+x
        MR_aux.append(a1)
    MR.append(MR_aux[:])

for i in range(len(MR)):
    print(MR[i])