alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8','9', '0']
word = input('Frase a ser descriptografada: ')
key = (int(input('Chave: '))%36)
word1 = list(word)
word2 = []
for i in range(len(word1)):
    for j in range(len(alfabeto)):
        if word1[i] == (alfabeto[j]):
            word2.append(alfabeto[j-key])
            break
        elif word1[i]== ' ':
                word2.append(' ')
                break
word3 = ''.join(word2)
print('frase descriptografada: ', word3)
