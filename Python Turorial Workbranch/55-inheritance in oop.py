
# inheritance = 1 - direct(child from parrent) 2- indirect(child from child )

class A:
  def __init__(self,color,model):
    self.color=color
    self.model=model

  def a_sound(self):
    print("AAAAAAAAAAA")


class B(A):
  def b_sound(self):
    print("BBBBBBBBB")



class C (B):
  def c_sound(self):
    print("CCCCC")

  
# create obj for testing 

x=C('red','x4')
x.a_sound()
x.b_sound()
x.c_sound()


