# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# l=[]
# l1=[]
# while i<len(a):
#     if a[i]%2==0:
#         l.append(a[i])
#     else:
#         l1.append(a[i])
#     i+=1
# print(l)
# print(l1)

# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# l=[]
# l1=[]
# mul=1
# while i<len(a):
#     mul=mul*a[i]
#     i+=1
#     print(mul,end=" ")

# a=[0,1,2,3,4,5,6,7,8,9,10,1,555,2]
# max=0
# min=1000
# i=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     if a[i]<min:
#         min=a[i]
#     i+=1
# print(max)
# print(min)

# a=[22,3,5,1,4,7,3,0,6]
# a.sort(reverse=True)
# print(a)
# max=0
# min=100
# sm=0
# tm=0
# i=1
# while i<=10:
#     user=int(input("enter the number:"))
#     if user>max:
#         max=user
#     if user<min:
#         min=user
#     if user>sm and sm<max:
#         sm=user
#     if user>tm and tm<sm:
#         user=tm
#     i+=1
# print(min)
# print(max)
# print(sm)
# print(tm)
# user=int(input("enter the number:"))
# for i in range(1,11):
#     print(user,"*",i,"=",user*i)