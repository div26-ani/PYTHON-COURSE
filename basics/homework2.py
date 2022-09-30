x=[]
y=0
for i in range(10):
    n=float(input('enter item in the item'))
    x.append(n)
print('the value entered is')
print(x)

for i in range(10):
    y=y+x[i]


mean=y/10
print("mean is-",mean)

if len(x)/2==0:
    median=(y+1)/2
    print("median is-",median)
else:
    median=((y/2)+((y/2)+1))/2
    print("median is-",median)

