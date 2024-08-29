import ShortCuts
a = list(input('DNA Strip: '))
a.reverse()
a = ''.join(str(i)for i in a)
print(ShortCuts.DNAReplacing(a))

