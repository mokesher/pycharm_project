import sys

line = [ int(i) for i in sys.stdin.readline().strip('\n') ]
set1 = set(line)

res = []


for x in line:
    for y in line:
        for z in line:
            if (x != y) and (y != z) and (z != x):
                res.append(x*100 + y*10 + z)



print(res)
print(len(res))
print(len(set(res)))


