import MyFunctions
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
MR = MyFunctions.MtrxCrt(LineQunt_m1, ClumQunt_m1)
for i in range(LineQunt_m1):
    for j in range(ClumQunt_m1):
        MR[i][j] = float(M1[i][j])+float(M2[i][j])
for row in range(LineQunt_m1):
    print(MR[row])
