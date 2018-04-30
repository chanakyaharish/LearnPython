#1
def f1():
    for i in range(150,271,5):
        if(i%7==0):
            print(i)

#2
def f2(nums):
    j=0
    for i in range(len(nums)):
        if(nums[i]%2==0):
            j=j+1
    print("Number of even numbers:",j)
    print("Number of odd numbers:",len(nums)-j)
 
#3   
def f3():
    for i in range(10):
        print(str(i)*i)
#4
def f4():
    n=int(input('enter input'))
    d={}
    for i in range(1,n+1):
        d[i]=i*i
    return d

#5
def f5(n):
    sum=1
    for i in range(1,n+1):
        sum=sum*i
    return sum

#6
import math
def f6(n):
    if(n<=1):
        return False
    
    for i in range(2,math.ceil(math.sqrt(n))):
        if(n%i==0):
            return False
    return True
