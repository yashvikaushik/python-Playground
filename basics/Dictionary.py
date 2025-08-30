# d1={1:10,2:20,3:30,4:40}
# d2={5:50,6:60,7:70,8:80}

# d3=d1 #now items of both d1 and d3 are same bcz of the concept of deep copy
# d3.update(d2)
# print(d3)
# sum=0
# for i in d1:
#      sum+=d1[i]
# print(sum)


# count the frequency of elements in a list
# l=[1,1,1,1,2,2,3,3,3,3,4,4,4,4,4,4,4]
# d={}
# for i in l:
#         if(i in d):
#             d[i]+=1
#         else:
#             d[i]=1
# print(d)

#combining two dictionaries by adding the values for common key
d1={1:10,2:20,3:30,4:40}
d2={4:50,5:50,6:60,7:70}
for i in d2.keys() & d1.keys():
        d1[i]+=d2[i]
        d2.pop(i)
d1.update(d2)
print(d1)
