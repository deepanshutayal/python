i=int(input('enter the year'))
if i%4==0:
	if i%100==0:
		if i%400==0:
			print('year is leap')
		else:
			print('year is not leap')
	else:
		print('year is leap')
	
else:
	print('year is not leap')
