num = int(input("Enter till the range to print the series : "))
a = 0
b = 1
for i in range(1, num + 1):
    print(a)
    b = a + b
    a = b - a
