# def printPerson(data):
#     for x,y in data.items():
#         print(x, ":", y)
# mydata={"name":"Manjusha",'age':56,'mobile':5555555}
# mydata['place']="india"
# printPerson(mydata)

# def printPerson(data):
#     print(data)
# userdata={}
# i=1
# while i !='0':
#     userkey=input("enter the key:")
#     uservalue=input("enter the value:")
#     userdata[userkey]=uservalue
#     i=input("enter zero to exist or any key to continue adding")
# printPerson(userdata)

# def printPerson(data):
#     for x,y in data.items():
#          print(x, ":", y)
# userdata={}
# i=1
# while i !='0':
#     userkey=input("enter the key:")
#     uservalue=input("enter the value:")
#     userdata[userkey]=uservalue
#     i=input("enter zero to exist or any key to continue adding")
# printPerson(userdata)


def printPerson(data):
    hkl=0
    for kl,vl in data.items():
        if hkl<len(kl):
            hkl=len(kl)
    for k,v in data.items():
        if hkl==len(k):
            print(k, ":", v)
        else:
            space=''
            balancekey_len=hkl-len(k)
            for kv in range(balancekey_len):
                space+=' '
            print(k+space,":",v)
userdata={}
i=1
while i !='0':
    userkey=input("enter the key:")
    uservalue=input("enter the value:")
    userdata[userkey]=uservalue
    i=input("enter zero to exist or any key to continue adding")
printPerson(userdata)


#     print(kl,len(kl),hkl)
# print(hkl)