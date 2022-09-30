def marks (**data):
    with open('marks.txt','a') as f:
        for n,m in data.items():
            f.write(f'{n}:{m}')

marks(rajesh=200,brijesh=120)
marks(raj=130,ajay=120,suraj=60,chand=155)
marks()    


# anonymous function (by the use of lamba)
f = lambda x: x*3+x-5
print(f(5))
print(f(13))
print(f(3.613))

