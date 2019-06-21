m=int(input('enter minutes'))
if m > 60 or m == 60 :
	t=m/60
	r=m%60
	print('it contains ',t, 'hours and ',r, 'minutes' )
else :
	print('it contains 0 hours and ',m, 'minutes' )