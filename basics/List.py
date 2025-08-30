#Question 1 Checking posistive and negative in a list
# num=[]
# for i in range(0,10):
#     i=int(input())
#     num.append(i)
# print(num)
# neg=0
# pos=0
# for i in num:
#     if(i<0):
#         neg+=1
#     elif(i>0):
#         pos+=1
#     else:
#         pos+=1
# print("positive numbers: ",pos)
# print("negative numbers: ",neg)

#Question 2 mean of list elements
# nums=[]
# sum=0
# size=int(input("enter the number of elements you want to be present in the list: "))
# for i in range(size):
#     i=int(input())
#     nums.append(i)
#     sum+=i
# print(sum)
# print("mean is: ",(sum//size))

#Question 3 find the greatest element and print its index too
# nums=[]
# sum=0
# size=int(input("enter the number of elements you want to be present in the list: "))
# greatest=0
# for i in range(size):
#     i=int(input())
#     nums.append(i)
# idx=0

# print(nums)
# for i in range(size):
#     if(greatest<nums[i]):
#         greatest=nums[i]
#         idx=i
        
# print(f"greatest element of the list is {greatest} found at {idx}")

#Question 4 to check if a list is sorted or not 
# nums=[]
# size=int(input("enter the number of elements you want to be present in the list: "))
# for i in range(size):
#     i=int(input())
#     nums.append(i)

# for i in range(size-1):
#     if(nums[i]<nums[i+1]):
#         res=True
#     else:
#         res=False
#         break
# else:
#     print("the list is sorted")

