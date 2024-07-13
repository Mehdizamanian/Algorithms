#write an app that get infinit numbs 
#print bigest one till inputing 0



x = int(input('numb : '))

while x>0:
	
	y= int(input('numbs  : '))
	
	
	if y==0:
		print('app finished successfully')
		break 
	
	
	
	if x>y :
		c=x
	else:
		c=y


print(c)

	
	