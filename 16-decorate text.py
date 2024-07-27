
# decorate text with no argoman app 

def message():
  return f'welcome ali to your website '



def decorator(func):
  
  def wrapper():

    print('***********')
    
    print(func())

    print('***********')
    
  return wrapper
  



decorator(message)()