#default parameter must come after required parameter
def total(a, b=3, c=0):
    return a + b + c
#named parameter must come after positional parameter
print(total(5))
print(total(a=5))

print(total(100,50))
print(total(a=100, b=50))
print(total(b=50, a=100))   # swapped and working

print(total(10,10,10))
print(total(a=10,b=10,c=10))
print(total(a=10,b=10,c=10))


def mean(*numbers):
    print(numbers)
    print(type(numbers))

mean(1,2,3,4)


def mean(*numbers):
    return sum(numbers)/len(numbers)

print(mean(1,2,3,4))
print(mean(1,22,1,1,2,3,32,231,312))
print(mean())




 