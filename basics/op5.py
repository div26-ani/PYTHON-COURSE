print('IN OPERATOR')
# IN operator with list operator
names=['divya','vineeta','suneeta']
print('divya' in names)
print('ankit' in names)
print('vineeta' in names)

# In operator with string datatype
message='once upon a time in mumbai, there was a lion'
print('upon' in message)
print('mumbai' in message)
print('there was' in message)

print('IS OPERATOR')

x=10
y=10
z=5
c=6
d=10
print(x is y)
print(x is c)
print(x is z)
print(y is z)
print(y is x)
print(c is x)
print(c is c)
print(c is d)
print(x is d)





print('Good ex. of IS OPERATORS')
x=[1,2,3]
y=[1,2,3]
z=x
print(x is y)
print(x is z)
print(z is y)