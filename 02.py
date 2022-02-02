list=input().split()
if len(list)%2==0:
    for i in range(0,len(list),2):
        list[i],list[i+1]=list[i+1],list[i]
else:
    for i in range(0,len(list)-1,2):
        list[i],list[i+1]=list[i+1],list[i]
print(list)
