# tuple - set -list (interchangeable)


x = [1,2,3,4,5,6,6,7]
xt = tuple(x)  #list->tuple
xl = list(xt)
xs = set(x)
xl = list(xs)
xl = set(xt)
xt = tuple(xs)


# wap to create tuple, by taking ten inputs from the user
x = []
for i in range(10):
    n=(input("enter the input"))
x.append(n)

print(x)
xl = tuple(x)
print(xl)