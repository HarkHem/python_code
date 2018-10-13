import sys

#out = sys.stdout
#sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'a')
s = list()
second = list()
n = int(input())
i = 0
while i < n:
    k = int(input())
    if k < 0:
        s.remove(-k)
    elif k == 0:
        second.append(s[0])
        del s[0]
        
    else:
        s.append(k)
    i=i+1
for x in second:      
    print(x)
sys.stdout.close()
    
        
