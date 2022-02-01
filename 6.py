import random
import string

def get_key(val,dict):
    for key, value in dict.items():
        if val == value:
            return key

    return "key doesn't exist"

length=random.randint(1,100)
letters = string.ascii_letters
randomkeys=[]
randomlist=[]
for i in range(length):
    randomkeys.append(''.join(random.choice(letters) for i in range(0,random.randint(1,10))))
    randomlist.append(random.randint(0,10))

total=dict(zip(randomkeys, randomlist))
num={
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0
}
meghdar={}
for count,value in enumerate(total):
    num[total[value]]+=1
    if 3<=len(value) and len(value)<=5:
        meghdar[value]=total[value]
print(num)
print(get_key(max(total.values()),total))
print(meghdar)

