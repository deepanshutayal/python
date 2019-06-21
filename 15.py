m=int(input('enter five digit no. '))

x=m%10
y=(x+1)
m=m//10

x=m%10
y=y+10*(x+1)
m=m//10

x=m%10
y=y+100*(x+1)
m=m//10

x=m%10
y=y+1000*(x+1)
m=m//10

x=m%10
y=y+10000*(x+1)


print(' no. becomes ',y)