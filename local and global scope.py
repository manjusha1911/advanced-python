# def manjusha():   #local
#     # global a      #it will become global
#     a="manjusha"
#     print(a)
# manjusha()

# a="manjusha"    #global
# def manjusha():
#     print(a)
# manjusha()


# a="manju"
# def manjusha():
#     global a
#     a="manjusha"
#     print(a)
# manjusha()
# print(a)


a="manju"
def manjusha():
    global a
    global b
    a="sai"
    b="manjusha"
    print(a)
manjusha()
print(a)
print(b)