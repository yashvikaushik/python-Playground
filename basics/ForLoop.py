# Question 1. printing the table of 5
# for i in range(1,11):
#     print("5 x ",i," = ",(5*i))

# Question 2. Accept an integer and print hello world n times
# n=int(input("enter a number to print hello world that many times: "))
# for i in range(n):
#     print(i+1," Hello World! ")

#Question 3. reverse for loop and print n to 1
# n=int(input("enter till what number you wnat to print the numbers in reverse order: "))
# for i in range(n,0,-1):
#     print(i,end=" ")

#Question 4. sum upto n numbers
# n=int(input("enter a number to calculate the sum till that number"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(f"sum = {sum}")

#Question 5 factorial of a number
# n=int(input("enter a number to calculate its factorial: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f"factoria of {n} is : {fact}")

#Question 6 to check if a number is perfect or not
# num=int(input("enter the number to be checked: "))
# fact=1
# for i in range(1,num):
#     if(num%i==0):
#         fact*=i
# if(num==fact):
#     print("perfect number")
# else:
#     print("not a perfect number")

#Question 7 check whether a number is a prime number or not
#using for loop break and else
# num=int(input("Enter the number to be checked: "))
# for i in range(2,num):
#     if(num%i==0):
#         print("not a prime number")
#         break
# else:
#     print("a prime number")

#Question 8 reversing a string
# string=input("enter a string or word of your choice: ")
# length=len(string)
# newstr=""
# for i in range(length-1,-1,-1):
#      newstr+=string[i]
# print("new string is : ",newstr)
# if(string == newstr):
#      print("palindroome")
# else:
#      print("not palindrome")

#Question 9 count all letter symbols and alphabets in a given string
# str=input("enter a string of your choice: ")
# ca=0
# cn=0
# cs=0
# for i in str:
#     if(i.isalpha()):
#         ca+=1
#     elif(i.isalnum()):
#         cn+=1
#     else:
#         cs+=1
# print("number of letters is: ",ca)
# print("number of numbers is: ",cn)
# print("number of special characters is: ",cs)

