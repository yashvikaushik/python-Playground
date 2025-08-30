import random
num=random.randint(1,10)
tries=0

while True:
    guess=int(input("please guess the number: "))
    if(num==guess):
          print("success")
          break
    elif(num<guess):
         print("go a lil lower")
         tries+=1
    elif(num>guess):
         print("go a lil higher")
         tries+=1
    else:
         print("failure ")
         tries+=1
print(f"you took {tries} tries to guess the number correctly")

