# we can make set from a list
# output: {1,2,3}
my_set = set([1,2,3,5])
print(my_set)


# set cannot have duplicates
# output : {1,2,3,4}
my_set = {1,2,3,4,3,2}
print(my_set)


# initialize my_set
my_set = {1,3}
print(my_set)

# add an element 
# output: {1,2,3}
my_set.add(2)
print(my_set)
  
# add multiple elements
# output: {1,2,3,4}
my_set.update([2,3,4])
print(my_set) 

# add list and set
# output: {1,2,3,4,5,6,8}
my_set.update([4,5],{1,2})
print(my_set)


# removing items from set
# initialize my_set
my_set = {1,3,4,5,6}
print(my_set)

# discard an element
# output:{1,3,5,6}
my_set