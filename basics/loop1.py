names = ['divya', 'ananya', 'pankaj', 'vineeta', 'ankit', 'aman']
for name in names:
    print("=>",name)

    msg ='once upon time in lucknow'
    for char in msg:
        print(char)

# stop
for i in range(100):
    print(i, end=' ')

# start/stop
for i in range(10,21):
    print(i, end='x')

# start/stop/step
for i in range(1,11,2):
    print(i, end='✔')


# reverse gap
for i in range(100, 0, -1):
    print(i, end=' ')


data = [2,5,9,6,2,3,6,5,9]
for i,d in enumerate(data):
    print(i,d)

print('=>')
data = ['apple', 'cheery', 'banana', 'samosa'] 
for i,d in enumerate(data):
    print(i+1,d)   


names = ['apple', 'banana', 'kiwi', 'cheery']
price = [100, 60, 500, 250]
for n, p in zip(names, price):
    print(f'' {n} => ${p}'')


    
