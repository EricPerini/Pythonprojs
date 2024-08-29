def Quanty(s):
    a = s.count("G")
    b = s.count("C")
    return (a+b)
File = open("C:/Users/perin/Downloads/rosalind_gc.txt", 'r')
Content = File.read()
File.close()
C = Content.splitlines()

a = []
for i in C:
    if i.count('>')>0:
        b = []
        b.append(i)
    else:
        b.append(i)
    if len(b)==17:
        a.append(b)
        b = []

for i in a:
    Total = 0
    GCCounter = 0
    for j in i:
        if j.count('>')>0:
            continue
        else:
            Total+=len(j)
            GCCounter+=Quanty(j)
    i.append((GCCounter/Total)*100)

Biggest = 0
Number = 0
for i in range(len(a)):
    if a[i][-1]>Number:
        Number = a[i][-1]
        Biggest = a[i][0]

print(Biggest)
print(Number)