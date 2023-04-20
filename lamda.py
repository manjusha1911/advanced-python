# def add(x,y):
#     return x+y
# result=add(25,30)
# print(result)     #normal method

# add=lambda a,b:(a+b)
# print(add(30,20))

# sub=lambda a,b:a-b
# print(sub(20,50))

# div=lambda a,b:a/b
# print(div(20,3))

# mul=lambda a,b:a*b
# print(mul(5,6))

# f_div=lambda a,b:a//b
# print(f_div(20,5))


# def eve(x):
#     return x%2==0
# l=[2,3,9,10,20,7,19,24,33,95,60]
# even=list(filter(eve,l))
# print(even)     #without lambda


def eve():
    return    #not required here we used only  for indentation
l=[21,32,90,10,20,7,19,24,33,95,60]
even=list(filter(lambda a:a%2==0,l))
print(even)