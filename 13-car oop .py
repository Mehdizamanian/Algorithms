# creating a complete car 


class Car :

  eng_status=True
  car_status=False
  current_speed=0

  def __init__(self,model,color,max_speed):
    self.model=model
    self.color=color
    self.max_speed=max_speed

  
  # methods
  def carinfo(self):
    print(f'Car model : {self.model}')
    print(f'Car color : {self.color}')
    print(f'Car max speed : {self.max_speed}')
    print(f'eng_status : {self.eng_status}')
    print(f'car_status : {self.car_status}')

  def carstarted(self,eng_status=eng_status,car_status=car_status):
    eng_status=self.eng_status
    car_status=self.car_status

    if eng_status==False:
      print('you need to fix your eng')
    
    
    elif eng_status==True and car_status==True:
        print('car is offed ')
        car_status=False
        return car_status


    elif eng_status==True and car_status==False:
        print('car is started successfully')
    



  def gaz(self,speed=10):
    max_speed=self.max_speed
    speed=self.current_speed+speed
    print(f'your current speed is increased : {speed}')

    if speed>max_speed:
        self.eng_status=False
        self.car_status=False
        self.current_speed=0
        

           


# creating obj
    
mehdi=Car('pride a4','red',80)

mehdi.carinfo()

mehdi.carstarted()

