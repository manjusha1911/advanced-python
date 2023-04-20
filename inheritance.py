# class a:    #parent class/base class
#     x="sai"
# class b:    #child class/derived class
#     y="manjusha"
# ob=a()
# ob1=b()
# print(ob.x)
# print(ob1.y )


# class a:
#     x="sai"
# class b(a):
#     y="manjusha"
# # ob=a()
# ob1=b()
# print(ob1.x)
# # print(ob1.y )


#  #single inheritance
 
# class Manju:
#     def M1(self):
#        print("Manjusha") 
# class Honey(Manju):
#     def M2(self):
#         print("Honey")
# obj=Honey()
# obj.M1()
# obj.M2()


#  #Multiple inheritance more than one inheritance 

# class Mom:
#     mom_name="vasundhara"
#     def mom(self):
#         print("Mother name:",self.mom_name)
# class Sis():
#     sis_name="mamatha"
#     def sis(self):
#         print("Sisternamr:",self.sis_name)        
# class Son(Mom,Sis):
#     child_name="Nany"
#     def son(self):
#         print("child namec:",self.child_name)
# obj=Son()
# obj.mom() 
# obj.sis()
# obj.son() 


#multilevel inheritance


class Sai:
    def sai(self):
        print("God")
class Vasu(Sai):
    def vasu(self):
        print("Mom")
class Child(Vasu):
    def child(self):
        print("child")
obj=Child()
obj.sai()
obj.vasu()
obj.child()