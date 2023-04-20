# a=9
# b=1
# print(a+b)
# print(int.__add__(a,b))

# a="sai"
# b="ram"
# print(a+b)
# print(str.__add__(a,b))


# class Student:
#     def __init__(self,m1,m2):
#        self.m1=m1
#        self.m2=m2
#     def  __add__(self,other):
#         m1=self.m1+other.m1
#         m2=self.m2+other.m2
#         return m1,m2
# s1=Student(30,50)
# s2=Student(20,50)
# s3=Student(30+20,50+50)
# print(s3.m1,s3.m2)
# # s3=s1+s2
# # print(s3)


class Student:
    def __init__(self,m1,m2):
       self.m1=m1
       self.m2=m2
    def  __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        return m1,m2
    def __gt__(self,other):  #it will compare the values
        s1tm=self.m1+self.m2
        s2tm=other.m1+other.m2
        if s1tm>s2tm:
            return True
        else:
            return False
s1=Student(30,50)
s2=Student(20,50)
s3=Student(30+20,50+50)
print(s3.m1,s3.m2)
# s3=s1+s2
# print(s3)
print("s1 TM:",s1.m1+s1.m2)
print("s2 TM:",s2.m1+s2.m2)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")