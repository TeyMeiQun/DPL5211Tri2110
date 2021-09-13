#student id：1201200152
#student name:tey mei qun
print("Invoice for Fruit Purchase")
print("-------------------------------------")

banana=float(input("enter the quantity (comb) of banana bought: "))
grape=float(input("enter the quantity (kg) of grape bought:  "))

price_b=banana*1.5
price_g=grape*5.6
total=price_b+price_g

print("Item                   QTY         PRICE     TOTAL")
print("BANANA(COMBS)          {}         RM1.50    RM{:.2F} ".format(banana,price_b))
print("GRAPE(KG)              {}         RM5.60    RM{:.2F} ".format(grape,price_g))
print("\nTotal:RM{:.2f}".format(total))
