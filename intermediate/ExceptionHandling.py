#exception handling try except finally and else block functioning
try:  #code that might have error
    a=10
    b=5
    c=a//b #divide by zero error
except Exception as e:
    print(e)

else: #runs only if no exception was caught
     print("no exception was caught")

finally: #this block of code will always run
    print("the finally block")


