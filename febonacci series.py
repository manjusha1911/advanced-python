def F(n):
    if n<=1:
        return n
    else: 
        return F(n-1)+F(n+2)
n=int(input("enter the number:"))
if n<=0:
    print()
else:
    print()
for i in range(n):
    print(F(i)) 
    
    
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
# nterms = 10
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))