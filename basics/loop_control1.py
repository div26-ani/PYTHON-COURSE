x = [1,2,3,4,5,6,7,8,9,0]


for i in x:
    if i == 0:
        if i == 0:
            continue
        print(i)


# continue with while


count = 1
while i <= 5:
    data = input('enter data:')
    if len(data) == 0:
        continue
    print(f'you entered a value of size {len(data)}')
    i += 1