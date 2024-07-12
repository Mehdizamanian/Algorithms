

#while(greatest nubert by getting 5 input)


x=int(input('num1 : '))
g=0


counter=2
while counter<=5 :
  y=int(input(f'num{counter} : '))
  if x>y:
    g=x
  else:
    g=y
  counter+=1

print(f'the greatest number is ===>   {g}')
  
