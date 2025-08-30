try:
    age=int(input("enter your age: "))
    if(age<18):
        raise WrongAge("invalid age")


except Exception as e:
    print(f"exception caught is: {e}")

else:
    print("no exception was found")

finally:
    print("the finally block")