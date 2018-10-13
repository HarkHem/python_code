import random

koloda = [6,7,8,9,10,2,3,4,11] * 4
random.shuffle(koloda)
gamers = input('How players \n')
print('Game?')
count = 0
s ={}
d = []
while True:
    choise = input('put cart y/n \n')
    if choise == 'y':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count > 21:
            print (count)
            break
        elif count == 21:
            print(count)
            break
        else:
            print('У вас %d очков' %count)
    elif choise =='n':
        print(count)
        break
d.append(count)
s[0]=count
player = count
i=0
while i < int(gamers):
    i=i+1
    count = 0
    koloda = [6,7,8,9,10,2,3,4,11] * 4
    random.shuffle(koloda)
    kol = random.randint(2,5)
    j=0
    while j < kol:
        j=j+1
        current = koloda.pop() 
        count += current
        if count > 21:
            print('игрок',i+1,'набрал',count,'очков')
            d.append(count)
            break
        elif count == 21:
            print('игрок',i+1,'набрал',count,'очков')
            d.append(count)
            break
        
    if count < 21:            
        print('игрок',i+1,'набрал',count,'очков')
        d.append(count)
    s[i]=count

d.sort()
k = 21
p = 0
while k > 0:
    if  d.count(k) == 0:
        k=k-1
        continue
    if  d.count(k) == 1:
        print('winer %d' %k)
        while p < (int(gamers)-1):
            if s[p] == k:
                print('player %d' %(p+1))
                break
            p = p + 1    
        break
    else:
        print('draw %d' %k)
        break
   
    

        


