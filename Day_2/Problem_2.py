n=int(input("Enter the value of N:"))
a=0
b=1
print("Fibonacci Series upto",n ,"is:")
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
    
