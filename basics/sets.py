s1={1,2,3,4,5,6,7,8,9,10}
s2={3,4,10,5,19,2,10}
print(s1)
s1.add(9)#duplicates not allowed
print(s1)#prints the original set

s1.add(100)#adds at the end of the set
print(s1)

#s1.remove(23)# shows an error bcz 23 is not present in the set
s1.discard(23) #shows no error

s1.discard(9)
print(s1)

if(3 in s1): #checking the memebership
    print("yes")
else:
    print("no")
union=s1.union(s2) #all elements of both sets but yes only the ones which are uniques bcx duplicates are not allowed
print(union)

intersection=s1.intersection(s2)#commom elements of both sets
print(intersection)

diff=s1.difference(s2)# removes s2 from s1
print(diff)

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list) #removes duplicates from a list
print("Unique elements:", unique_set)

