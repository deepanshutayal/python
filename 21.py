i=int(input('enter the year '))
if i%4==0 and i%100==0 and i%400==0 :
	print('year is leap')
else:
	if i%4==0 and i%100==0	and i%400!=0 :
		print('year is not leap')
	else:
		if i%4==0:
			print('year is leap')
		else:
			print('year is not leap')