def check_ev(n):
    if(n%2==0):
        return True
    else:
        return False
    
def check_odd(n):
    if(n%2!=0):
        return True
    else:
        return False
    
def check_prime(n):
    for a in range(3,n+1):
        if(n%a==0):
            return False
    else:
        return True 

def check_armstrong(n):
    order=len(str(n))
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10
    if(n==sum):
        return True
    else:
        return False
           
def check_palindrome(n):
    m1=str(n)
    m= m1[::-1]
    if(n==int(m)):
        return True
    else:
        return False

def numCheck():
    num=int(input("Enter the Number to be checked:"))
    if(check_ev(num)):
        print(num," is an Even Number")
    if(check_odd(num)):
        print(num," is an Odd Number")
    if(check_prime(num)):
        print(num," is a Prime Number")
    if(check_palindrome(num)):
        print(num," is a Palindrome Number")
    if(check_armstrong(num)):
        print(num," is an Armstrong Number")
numCheck()

