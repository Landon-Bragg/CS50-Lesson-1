##Comparing unknown integers from the user so we can make decisions in advance
x = int(input("What is x? "))
y = int(input("What is y? "))

#if x > y:
    #print("x is greater than y")
#elif x < y:
   # print("x is less than y")
#else:
    #print("x is equal to y")

if x < y or x > y:
    print("x is not equal to y")
else: 
    print("x is equal to y")
