k = int(input('K : ')) #Homo Dominant
m = int(input('M : ')) #Hetero
n = int(input('N : ')) #Homo recess
totalind = k+n+m
KChance = (((k*k)-k)/((totalind*totalind)-totalind))+((k*m)/((totalind*totalind)-totalind))+((k*n)/((totalind*totalind)-totalind))
MChance = ((k*m)/((totalind*totalind)-totalind))+((((m*m)*3)-(m)*3)/(((totalind*totalind)*4)-(totalind)*4))+((m*n)/(((totalind*totalind)*2)-(totalind)*2))
NChance = ((n*k)/((totalind*totalind)-totalind))+((m*n)/(((totalind*totalind)*2)-(totalind)*2))
print(KChance, MChance, NChance, KChance+MChance+NChance)
