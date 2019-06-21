x=float(input('enter the hardness '))
y=float(input('enter the carbon content '))
z=float(input('enter the tensile strength '))
if x>50 and y<0.7 and z>5600:
	print("grade 10")
elif x>50 and z>5600:
	print("grade 6")
elif  y<0.7 and z>5600:
	print("grade 8")
elif x>50 and y<0.7 :
	print("grade 9")
elif x>50 or y<0.7 or z>5600:
	print("grade 6")
else:
	print("grade 5")














