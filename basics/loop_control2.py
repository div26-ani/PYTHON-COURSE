while True:
    price = int(input('enter price of item:'))
    if price < 0:
        break
    print(f'you have entered {price} amount')


x = [1,2,3,4,5,6,7,8,-3,87,89]
for i in x:
    if i < 0:
        break
    print(i)