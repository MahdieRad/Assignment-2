A=int(input('Enter The Clock in Secends : '))
Hour=int(A/3600)
A=A%3600
B=int(A/60)
S=A%60
print(Hour,"/",B,"/",S)
