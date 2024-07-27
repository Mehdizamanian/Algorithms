# we use dc to decorate our code wich can be checking or proscess or ..... 

def decorator(func,x,y):
  return func(x,y)


def add(x,y):
  return x+y

def sub(x,y):
  return x-y


print(decorator(add,4,3))
print(decorator(sub,4,3))

#tip = for using dc you have to call just name with no () as u can see in line 15
#tip2 = we can use @ to call dc instead if dc()




