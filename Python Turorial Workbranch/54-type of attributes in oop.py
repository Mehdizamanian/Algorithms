

# instance attribute => magical method defines 

# class attribute or shared 


class Car:

  wheels=4
  
  def __init__(self,color,model):
    
    self.color=color
    self.model=model


  def info(self):
    print('color : ',self.color)
    print('model :',self.model)
    print('wheels : ',self.wheels)



# create obj

ali=Car('green','samand Z11')

mehdi=Car('red','prid L4')

mehdi.wheels=3
mehdi.info()