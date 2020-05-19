a=int(input("Runs scored by A:"))
b=int(input("Runs scored by B:"))
c=int(input("Runs scored by C:"))
#strike rate of each
str_rate1=(a/60)*100
str_rate2=(b/60)*100
str_rate3=(c/60)*100
#printing strike rate
print("Strike rate of player A is", str_rate1)
print("Strike rate of player B is", str_rate2)
print("Strike rate of player C is", str_rate3)
#runs if each of them they play 60 more balls 
print("Runs scored by player A if they played 60 more balls is", a * 2)
print("Runs scored by player B if they played 60 more balls is", b * 2)
print("Runs scored by player C if they played 60 more balls is", c * 2)
#Maximum Number of sixes each player could have hit
print("Maximum number of sixes player A could hit =", a // 6)
print("Maximum number of sixes player B could hit =", b // 6)
print("Maximum number of sixes player C could hit =", c // 6)

