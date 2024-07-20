

class Student :

  def __init__(self,name,fname,age,mark):
    self.name=name
    self.fname=fname
    self.age=age
    self.mark=mark

  def score(self,mark):
    if(mark>=10):
      print('he passed the course')
    else:
      print('he failed ')



# create object

mahdi=Student('mahdi','zamani',23,11)
print(mahdi.fname)

mahdi.score(4)