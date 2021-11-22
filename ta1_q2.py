import math
def sin(n,x):
    if(n==0):
        return x
    else:
        return -math.pow(x,2)*sin(n-1,x)/math.factorial(2*n*(2*n+1))
print("compute sin(x) using expansion: input x, n separated by space")
[x,n]=map(float,input().split())

print(sin(n,x))

