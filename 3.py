a=int(input("Input Number A :"))
b=int(input("Input Number B :"))
if a>b :
    Max=a
else:
    Max=b
for i in range(2,Max+1):
    if((a%i==0) and (b%i==0)):
        BMM=i
print("Result :  ", BMM)
