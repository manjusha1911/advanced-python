class manju:
    x=100     #class or static variables ,we can,t change value(only we can change with the class name(example here-- (manjusha.x=100)bellow object we have to take)
    def __init__(self):
        # y="honey"  #instance variable,we can change value
        self.name="manjusa"
        self.age=20
        self.place="blr"
obj=manju()
# obj.name="honey"
# obj.age=12
# obj.place="nlr"
manju.x=200
print(obj.name,obj.age,obj.place,manju.x)
