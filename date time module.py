# import datetime
# pt=datetime.datetime.now()
# print(pt)
# ct=datetime.datet ime.now()
# print(ct) 

# import datetime as dt
# ct=dt.datetime.now()
# print(ct)


# from datetime import*    #we use * in datedate very rare
# pt=datetime.now()
# print(pt)
# print(pt.year)

# import datetime as dt
# pt=dt.datetime.now()
# # f1=pt.strftime("%d-%m-%Y,%A")   #for full day
# f1=pt.strftime("%d-%m-%y,%a")  #for shortcut day like(mon,tue,wed,sun..etc)
# print(f1)

# import datetime as dt
# pt=dt.datetime.now()
# # f1=pt.strftime("%d/%m/%y,%A")
# # print(pt.strftime("on%A"))
# x=""
# if pt.strftime("%d")=="1" or pt.strftime("%d")=="31":
#     x="st"
# elif pt.strftime("%d")=="2":
#     x="nd"
# elif pt.strftime("%d")=="3":
#     x="rd"
#     print("YES")
# else:
#     x="th"
# print(pt.strftime("On %A"))
# print(pt.strftime("%d"+x+"%b %y"))
# print(pt.strftime("at %I:%M:%p"))


import datetime as dt
pt=dt.datetime(2022,12,31)
f1=pt.strftime("%d-%m-%y,%A")
print(f1)
if pt.strftime("%d")=="01" or pt.strftime("%d")=="31":
    x="st"
elif pt.strftime("%d")=="2":
    x="nd"
elif pt.strftime("%d")=="3":
    x="rd"
else:
    x="th"
print(pt.strftime("On%A"))
print(pt.strftime("%d"+x+"%b%Y"))