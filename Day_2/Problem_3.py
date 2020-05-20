n=int(input())
i=0
j=n-1
for row in range(n):
    for col in range(n):
        if row==i and col==j:
            print("*",end="")
            i+=1
            j-=1
        elif row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()
