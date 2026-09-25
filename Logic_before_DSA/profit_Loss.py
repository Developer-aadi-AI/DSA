cp = float(input("Enter the cost price : "))
sp = float(input("enter the selling price : "))

if sp >= cp :
    profit = sp - cp
    per = ((sp - cp) / cp) * 100
    print(f"Profit is : {profit}rs\nprofit percentage is {per}%")
else:
    loss = cp - sp
    per = ((cp - sp) / cp) * 100
    print(f"loss is : {loss}rs\nloss percentage is {per}%")