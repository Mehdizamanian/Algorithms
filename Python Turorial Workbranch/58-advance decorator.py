
def decorator(func):
  def wrapper(*args,**kwargs):
    print("*************")
    fun=func(*args,**kwargs)
    print("*************")
    return fun
  return wrapper


@decorator
def message(x):
  print(f"Hello {x} welcome ")
  

@decorator
def num(x):
  print (str(int(x)+3))


# test app

x=input('enter your name  :  ')

message(x)

num(x)


