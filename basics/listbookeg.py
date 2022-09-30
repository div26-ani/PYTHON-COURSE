books = ['you can win', 'children knowledge bank', 's.chand', 'revolution2020']

books.append('The Final Empire')
books.append('Atomic Habit')
books.append('Steelheart')
books.append('Three mistakes if my life')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books[6] = 'i m the hero of my life'
books[-1] = 'hero of ages'
books[2] = 'legion'

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.insert(3, 'revolution:skin deep') 
books.insert(5,'blast')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| book')

