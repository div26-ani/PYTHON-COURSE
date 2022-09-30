my_dict = {1: 'apple', 2: 'ball'}
val_dict = {
    'employee': 'Rajendra Singh', 'age':30,
    'experience': 10, 'dept': 'Accounts',
    'designation': 'System Officer', 'salary': 60000,
    'team_size': 7
}
print(val_dict)

# retreival of value
ans = val_dict['designation']
print(ans)
print(val_dict['salary'])
print(val_dict['experience'])


# adding a data inside val_dict
val_dict['company'] = 'acme.inc'
print(val_dict)
from pprint import pp
pp(val_dict)
