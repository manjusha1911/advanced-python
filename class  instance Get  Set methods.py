class manjusha:
    def __init__(self):
        self.marks1="marks1"
        self.marks2="marks2"
        self.marks3="marks3"
    def get_m1(self):
        return self.marks1
s1=manjusha()
print(s1.get_m1())


class manjusha:
    def __init__(self):
        self.marks1="marks1"
        self.marks2="marks2"
        self.marks3="marks3"
        
     #get methods   
    def get_m1(self):
        return self.marks1
    
    
    def get_m2(self):
        return self.marks2
    
    
    def get_m3(self):
        return self.marks3
    
    #set methods
    def set_m1(self,value):
        self.marks1=value
        
        
    def set_m2(self,value):
        self.marks2=value  
        
        
    def set_m3(self,value):
        self.marks3=value
                 
s1=manjusha()
s1.set_m1(90)
s1.set_m2(85)
s1.set_m3(95)
print(s1.get_m1(),s1.get_m2(),s1.get_m3())
# print(s1.get_m1())
# print(s1.get_m2())
# print(s1.get_m3())


