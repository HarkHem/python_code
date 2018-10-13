x = input()
y = input()
x = x if x % 2 == 0 else x + 1
print("\n".join([str(num) for num in range(x, y +1 , 2)]))
