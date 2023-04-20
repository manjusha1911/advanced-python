class manjusha:
    school="jss"
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
    
    @classmethod     #decaratore 
    def get_schl(cls):  #self we have to take "cls" 
        return cls.school  
          
# s1=manjusha()
print(manjusha.get_schl())
# s1.set_m1(90)
# s1.set_m2(85)
# s1.set_m3(95)
# print(s1.get_m1())
# print(s1.get_m2())
# print(s1.get_m3())


