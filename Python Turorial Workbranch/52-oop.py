
# create a car blueprint to make objects on that 

# Attributes = (car size model speed ) that should be defined in a majical method to get attributes automaticllay  

# methoods= 1-standard 2- Majical



class Car:
  #tip = class should alwayes get self argoman in any types of methods to say this class
  #we use majical method(instructor)to get attributes and value them automaticlly while creating ong in line 23
  def __init__(self,color,ms,model):
    self.color=color
    self.maxspeed=ms
    self.model=model
  #we use stanard method to create functions or methods such as beep that shoud be called manually in line 27
  def horn(self):
    print('Beeeeep')

  # objs are the same variable that get a class in themselves


#-------------  NEW CRATE OUR OBJ BUILDING ON THE CLASS DEFINED ---------------------
    
mehdimachine=Car('red',50,'pride z4')

print(mehdimachine.color)

mehdimachine.horn()


