cp=float(input("Cost Price is:")) 
sp=float(input("Selling Price is:"))
profit=sp-cp
print("Profit is: ", profit)
#If profit is increased by 5%
sp=sp+((5/100)*profit)
print("SP after 5% increase in Profit is:",sp)
