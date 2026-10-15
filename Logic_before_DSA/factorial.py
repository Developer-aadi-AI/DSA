num = int(input("Enter a number : "))
fact = 1
if num >= 0:
    for i in range(2,num + 1):
        fact *= i
    print(fact)

else:
    print("Fact is not possible")

