for n in range(1,200):
   if all(n%i!=0 for i in range(2,n)):
      print(n) 