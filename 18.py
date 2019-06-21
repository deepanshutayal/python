n1=int(input('enter first no.'))
n2=int(input('enter second no.'))
n3=int(input('enter third no.'))
if n1==n2 :
	if n1==n3 :
		print('all three are equal')
	else:
		if n1>n3:
			print('first and second are largest')
		else:
			print('third is largest')
else :
		if n1==n3:
			if n1>n2:
				print('first and third are largest')
			else:
				print('second is largest')
		else:
			if n2==n3:
				if n2>n1:
					print('second and third is largest')
				else:
					print('first is largest')
			else:
				if n1 > n2 :
					if n1 > n3 :
						print(" First Number is Largest ")
					else :
						print( " Third Number is Largest ")
				else :
					if n2 > n3 :
						print(" Second Number is Largest ")
					else :
						print( " Third Number is Largest ")
	