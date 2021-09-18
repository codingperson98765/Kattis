# Link to kattis problem https://open.kattis.com/contests/qo87nq/problems/conundrum

line = input()
a = 0
b = 1
c = 2
day= 0

for i in range(0,len(line),3):
    if line[a] != 'P':
        day+=1
    if line[b] != "E":
        day+=1
    if line[c] != "R":
        day+=1
    a += 3
    b += 3
    c += 3
    
print(day)    
    
