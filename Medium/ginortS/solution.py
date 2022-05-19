S = input()
u = []
l = []
o = []
e = []
for i in S:
    if i.isupper(): u.append(i)
    elif i.islower(): l.append(i)
    elif i.isdigit:
        if int(i)%2 != 0:
            o.append(i)
        else:
            e.append(i)

result = ''.join(sorted(l))+''.join(sorted(u))+''.join(sorted(o))+''.join(sorted(e))

print(result)
