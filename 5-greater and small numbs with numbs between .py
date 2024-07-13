
#write app print int between numbs 


x=int(input('enter num  1   :  '))

counter =2
while counter<=2:
	y=int(input(f'enter num  {counter}   :  '))
	if x>y:
		g=x
		s=y
	else:
		g=y
		s=x
	counter+=1
	
	

print(f'big  :   {g}  and  small  :  {s}')



while s <=g:
	print(s)
	s+=1
	
	
	
	
