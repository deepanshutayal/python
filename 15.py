m=int(input('enter five digit no. '))

x=m%10
a=(x+1)
m=m//10

x=m%10
b=(x+1)
m=m//10

x=m%10
c=(x+1)
m=m//10

x=m%10
d=(x+1)
m=m//10

x=m%10
f=(x+1)
y=(10000*f)+(1000*d)+(100*c)+(10*b)+a

print(' no. becomes ',y)