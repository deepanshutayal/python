x=int(input('enter the company stock '))
y=int(input('enter the customer order '))
z=input('enter customer credit ')
if y<=x and z=='ok' :
	print('supply has requirment')
elif y>x and z=='ok' :
	print('supplied ',x,' balance ',(y-x))
else:
	print('credit not sufficient')















