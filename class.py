class Test:
    sv1 = 10
    sv2 = 102
    def __init__(self,initvar):
        self.Iv1 = 10
        self.Iv2 = initvar

        print(self.sv1)
        print(Test.sv2)

    def display(self):
        self.Iv2 = 30
        print(self.sv1)
        print(Test.sv2)
t1= Test(100)
print(t1.Iv2,t1.sv1,t1.sv2)
t1.sv1 = 10
print(t1.sv1)





'''
    t1 = Test(10,20)
print(t1.a)



class Human:

  def __init__(self,name):
      self.name = name

t1 = Human('ashish')
print(t1.name)
'''