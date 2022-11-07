nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
names = ['Amit Singh', 'Chadha Lal', 'Gunjan Pratap', 'Thakur Pratap Singh']

num_sqr = list(map(lambda i:i**2, nums))
print(num_sqr)

num_eq1 = list(map(lambda i: i+4 * i**2, nums))
print(num_eq1)

first_names = tuple(map(lambda nm: nm.split()[0], names))

print(first_names)
