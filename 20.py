
x=int(input('enter the x- axis centre point.'))
y=int(input('enter the y- axis centre point.'))
r=int(input('enter the radius'))
x1=int(input('enter the x- axis  point.'))
y1=int(input('enter the y- axis point.'))
z=(((x1-x)**2)+((y1-y)**2))**1/2
if r>z:
	print('point lies inside')
else:
	if z==r:
		print('point lies on circle')
	else:
		print('point lies outside')
