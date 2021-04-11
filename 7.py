List=[]
print('Enter 20 numbers :')
for i in range(20):
    A = int(input())
    List.append(A)
    List[i]**= 2
print('Numbers ^ 2 :'+str(List))
List_min = List[0]
List_max = List[0]
for j in range(1,20):
    if List[j]>List_max:
        List_max=List[j]
    else:
        List_min=List[j]

print('Min Number '+str(List_min))
print('Max Number: '+str(List_max))
