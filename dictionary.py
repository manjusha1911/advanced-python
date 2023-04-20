# a={"name":"manjusha","age":10,"place":"bangalore"}
# print(a["name"])

# a={"name":"manjusha","age":10,"age":11,"place":"bangalore"}
# print(a)

# a={"name":"manjusha","age":10,"mobile":0.00  ,"place":"bangalore"}
# a["mobile"]=9380766651
# print(a)
# a={"name":"manjusha","age":10,"mobile":0.00  ,"place":"bangalore"}
# a["occupation"]="software"
# print(a)

# a={"name":"manjusha","age":10,"mobile":0.00  ,"place":"bangalore"}
# a.update({'name':"sai"})
# a.update({'dob':2000}) 
# print(a)

# a={"name":"manjusha","age":10,"mobile":0.00  ,"place":"bangalore"}
# a.pop("age")
# print(a)

# a={"name":"manjusha","age":10,"mobile":0.00  ,"place":"bangalore"}
# del a["name"]
# print(a)
# del a
# print(a)

# a={"name":"manjusha","age":10,"mobile":0.00  ,"place":"bangalore"}
# a.clear()
# print(a)

# a={"name":"manjusha","age":10,"mobile":0.00  ,"place":"bangalore"}
# print(a.keys())
# print(a.values())

a={"name":"manjusha","age":10,"mobile":0.00  ,"place":"bangalore"}
if "name" in a:
    print("YES")
else:
    print("NO")