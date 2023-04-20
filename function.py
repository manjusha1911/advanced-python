# def manjusha(a):
#     print("manjusha")
# manjusha()n

# def manjusha(a):
#     print("manjusha")
# manjusha("manju")

# def manjusha(a,b):
#     print(a+b)
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# manjusha(a,b)

# def manjusha(name="user"):
#     print(name)
# manjusha()

# def manjusha(a,b):
#     result =(a+b)
#     print(result)
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# manjusha(a,b)

# def manjusha(a,b):
#     result =(a+b)
#     print(result)
# manjusha(39,10)

# def manjusha(*x):
#     result=0
#     for a in x:
#         result+=a
#     print(result)
# # a=int(input("enter the number:"))
# # b=int(input("enter the number:"))
# # manjusha(a,b)
# manjusha(39,10)    #we can take n number of arguments

# def manjusha(name,age):
#     print(name,age)
# manjusha("manjusha",20)
# def manjusha(name,age):
#     print(name,age)
# manjusha(age=36,name="manjusha")

# def manjusha(name,age,country="india"):
#     print(name,age,country)
# manjusha(age=36,name="manjusha")
# manjusha(country="uk",name="v",age=25)

# def manjusha(*num):
#     result=0
#     for x in num:
#         result+=x
#     return result
# sai=manjusha(20,10,30,25,36)
# print(sai)

def manjusha(*num):
    result=0
    var=99
    for x in num:
        result+=x
    return result,var
# sai=manjusha(20,10,30,25,36)
sai,manju=manjusha(20,10,30,25,36)
print(sai,manju)

