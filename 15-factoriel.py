
#solution  4=4X3X2X1


x=int(input('number   :   '))


def factorial(x):
  x+=1
  f=1
  while x>1:
      x-=1
      print(x ,end="")
      f=f*x
  print (f'  ==>  Factorial is : {f}')
  


factorial(x)



