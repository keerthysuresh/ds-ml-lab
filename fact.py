print("demo of function:programto find factorial of a number")
def fact(n):
    if n==1:
        return 1
    else:
        return(n* fact(n-1))
n=int(input("enter a number:"))
print("factorial:",fact(n))
