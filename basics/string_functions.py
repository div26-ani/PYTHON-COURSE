newData='Hello! guys this is mumbai and this is my dream city.I love to explore this city many more times.'
print(newData.lower())
print(newData.upper())
print(newData.swapcase())
print(newData.casefold())
print(newData.capitalize())
print(newData.title())


print('lower =>',newData.lower())
print('upper=>',newData.upper())
print('swapcase=>',newData.swapcase())
print('title=>',newData.title())


word='HELLO!'
spacing = 20
ljust = word.ljust(spacing,'#')
print(ljust)


rjust = word.rjust(spacing,'_')
print(rjust)


cen=word.center(spacing,'%')
print(cen)


# validation functions - either True or False
print(newData.isupper())
print(newData.islower())
print(newData.isalpha())
print(newData.isnumeric())
print(newData.isalnum())

# utility functions
idx = newData.find("mumbai")
if idx==-1:
    print('not found')
else:
    print(f'mumbai was found at index{idx}')
    
