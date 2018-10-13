import random

koloda = [2,3,4,6,7,8,9,10,11] * 4
random.shuffle(koloda)
players = input('how many players? \n')
firstcard = koloda.pop()
summa = firstcard
print('you cart',firstcard)
while True:
    choise = input('put cart y/n \n')
    if choise == 'y':
        card = koloda.pop()
        print('you cart',card)
        summa = summa + card
        print('you sum',summa)
        if summa > 21:
            print (count)
            break
        elif summa == 21:
            print(count)
            break
        
    elif choise =='n':
        print('you finish sum',summa)
        break
    
