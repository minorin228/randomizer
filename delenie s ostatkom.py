import random
a=int(input('кол-во вариантов - '))
b=int(input('Кол-во человек - '))
c=int(a/b)
c1=int(a%b)
print (c1)

m=[]
for i in range(a):
    i+=1
    m.append(i)
random.shuffle(m)
print(m)

i=0
y=1
if c1!=0:
    print('kod na dorabotke')
else:
    if c == 6:
        while i != a:
            print(m[i], m[i + 1], m[i + 2], m[i + 3], m[i + 4], m[i + 5], 'Номер по списку  - ', y)
            i += c
            y += 1
    elif c == 5:
        while i != a:
            print(m[i], m[i + 1], m[i + 2], m[i + 3], m[i + 4], 'Номер по списку  - ', y)
            i += c
            y += 1
    elif c == 4:
        while i != a:
            print(m[i], m[i + 1], m[i + 2], m[i + 3], 'Номер по списку  - ', y)
            i += c
            y += 1
    elif c == 3:
        while i != a:
            print(m[i], m[i + 1], m[i + 2], 'Номер по списку  - ', y)
            i += c
            y += 1
    elif c == 2:
        while i != a:
            print(m[i], m[i + 1], 'Номер по списку  - ', y)
            i += c
            y += 1
    elif c == 1:
        while i != a:
            print(m[i], 'Номер по списку  - ', y)
            i += c
            y += 1
