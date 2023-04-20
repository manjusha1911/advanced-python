# class Apple:
#     x=99    #inside we can take properties and methods
# obj=Apple()
# print(obj.x)



# class Apple:
#     x=99    #inside we can take properties and methods
#     def sm(self):
#         print(self.x)
# obj=Apple()   #we should take this
# obj.sm()


# class Apple:
#     x=99    #inside we can take properties and methods
#     def sm(self):
#         print(self.x)
# obj=Apple()
# Apple.sm(obj)



# class Py:
#     def sam(self):
#         print("samsung")
#     def ex(self):
#         print("Apple")
# obj=Py()
# obj.ex()
# obj.sam()

# class mobile:
#     def __init__(self,brand,rom,ram):
#         self.brand=brand
#         self.rom=rom
#         self.ram=ram
#     def mb(self):
#         print(self.brand,self.rom,self.ram)
# obj=mobile("iphone11",12,256)
# obj.mb()
        
        
        
# class mobile:
#     def __init__(self):
#         self.brand="brand"
#         self.ram="ram"
#         self.rom="rom"
#     def info(self):
#         print(self.brand,self.ram,self.rom)
# obj=mobile()
# obj.info()


class mobile:
    def __init__(self):
        self.brand="brand"
        self.ram="ram"
        self.rom="rom"
    def info(self):
        print("model :",self.brand)
        print("ram   :",self.ram)
        print("rom   :",self.rom)
obj=mobile()
obj.info()
    