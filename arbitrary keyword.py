# def person(*data):
#     print(data)
# person("sai","manjusha",24,9846473641)

# def person(**data):
#     print(data)
#     for k,v in data.items():
#         if k=="god":
#             print(k, "   :", v)
#         elif k=='name':
#             print(k, "  :", v)
#         elif k=="age":
#             print(k,"   :", v)
#         else:
#             print(k, ":", v)
# person(god="sai",name="manjusha",age=24,mobile=9846473641)

# def person(**data):
#     print(data)
#     print("")
#     for k,v in data.items():
#         if k=="god":
#             print(k, "   :", v)
#         elif k=='name':
#             print(k, "  :", v)
#         elif k=="age":
#             print(k,"   :", v)
#         else:
#             print(k, ":", v)
# god=input("enter the god's name:")
# name=input("enter the name:")
# age=int(input("enter the age:"))
# mobile=int(input("enter the mobile number:"))
# print("")
# person(god=god,name=name,age=age,mobile=mobile)   #we can take different variable name



def person(**data):
    print(data)
    print("")
    for k,v in data.items():
        if k=="god":
            print(k, "   :", v)
        elif k=='name':
            print(k, "  :", v)
        elif k=="age":
            print(k,"   :", v)
        else:
            print(k, ":", v)
i=1
while i!=0:
    god=input("enter the god's name:")
    name=input("enter the name:")
    age=int(input("enter the age:"))
    mobile=int(input("enter the mobile number:"))
    print("")
    person(god=god,name=name,age=age,mobile=mobile)   #we can take different variable name
    i=int(input("enter the i value:"))
print("end")
