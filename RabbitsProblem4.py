#Months
MonthsQuatity = int(input('Months: '))

#Rabbits by litter
k = int(input('Rabbits by litter: '))

YoungRabbits = 1
AdultRabbits = 0
MiddleAge = 0
Result = 0
for i in range(MonthsQuatity):
    AllRabbits = YoungRabbits+AdultRabbits+MiddleAge
    if AllRabbits==1:
        if MiddleAge==1:
            AdultRabbits += MiddleAge
            MiddleAge -= MiddleAge
        if YoungRabbits==1:
            MiddleAge += YoungRabbits
            YoungRabbits -= YoungRabbits
    if AllRabbits>=1:
        if AdultRabbits>=1:
            YoungRabbits += AdultRabbits*k
        if MiddleAge>1:
            AdultRabbits +=MiddleAge
            MiddleAge-=MiddleAge
        if YoungRabbits>1:
            MiddleAge += YoungRabbits
            YoungRabbits-=YoungRabbits
    Result = AllRabbits

print(f'Result: {Result}')
