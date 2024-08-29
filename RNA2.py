RNA = input('RNA strip: ')
RNAList = list(RNA)
RNAResult = []
for i in range(len(RNA)):
    if RNAList[i]=='T':
        RNAResult.append('U')
    else:
        RNAResult.append(RNAList[i])
RNAResult = ''.join(str(i)for i in RNAResult)
print(RNAResult)

#s = input() 
#print(s.replace("T", "U"))