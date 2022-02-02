FLine=input()
SLine=input()
ans=0
for count, value in enumerate(FLine):
    if value!=SLine[count]:
        ans+=1
print(ans)
