a=int(input("Input Number A :"))
b=int(input("Input Number B :"))
if a<b:
    Max=b
else:
    Max=a
for i in range(Max , (a*b)+1):
    if i%a==0 and i%b==0:
        KMM=i
        break
print("Result: ", KMM)
