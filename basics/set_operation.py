# set union
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# use | operator
# output: {1,2,3.4,5,6,7,8}
print(A|B)

# use union fun
print(A.union(B))

# use union function on B
print(B.union(A))

# intersection
# use & operator
print(A & B)


print(A.intersection(B))


# set difference
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# use - operator on A
print(A-B)
 
print(A.difference(B))

print(B-A)

# symmetric difference
# use ^ operator
print(A ^ B)

print(A.symmetric_difference(B))