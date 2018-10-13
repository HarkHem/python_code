year = input()
amount = input()
rate = input()
for i in range(year):
    amount=(amount * rate / 100 ) + amount
    print("year:", i + 1," amount:", amount)
