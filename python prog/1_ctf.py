def IsPrime(n):
   d = 2
   while n % d != 0:
       d += 1
   return d == n

a = input();
if(a==1):
    print(False)
else:
    print(IsPrime(a))
