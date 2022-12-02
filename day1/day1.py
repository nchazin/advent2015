import sys

with open(sys.argv[1]) as f:
    data = f.read().strip()

ops = [a for a in data]


floor = 0

for op in ops:
    if op == '(':
        floor += 1
    if op == ')':
        floor -= 1

print(floor)

pos = 1
floor = 0
for op in ops:
    if op == '(':
        floor += 1
    if op == ')':
        floor -= 1
    if floor < 0:
        print(pos)
        break
    pos+= 1
   


