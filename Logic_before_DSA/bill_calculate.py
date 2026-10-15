unit = int(input("Enter total unit : "))
amount = 0
if unit<0 :
    print("Invalid unit")
else:  
    if 0<unit<=100 :
        amount += 5 * unit
    elif 100<unit<=200:
        amount += ((5 * 100) + (7 * (unit - 100)))
    else:
        amount += ((5 * 100) + (7 * 100) + (10 * (unit - 200)))
    print("Amount is : ", amount)
