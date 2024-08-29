DNAStrip = input('DNA Strip: ')
DNAList = list(DNAStrip)
a = 0
c = 0
g = 0
t = 0
for i in range(len(DNAStrip)):
    if DNAList[i]=='A':
        a+=1
    elif DNAList[i]=='C':
        c+=1
    elif DNAList[i]=='G':
        g+=1
    elif DNAList[i]=='T':
        t+=1

print(a, c, g, t)

#def qt(s):
#     return s.count("A"), s.count("G"), s.count("C"), s.count("T")