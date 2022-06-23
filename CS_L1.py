##Ask user for their name
#name = input("What's your name? ")

##Remove whitespace from str and capitalize user's name
#name = name.strip().title()

##Say hello to user
#print("Hello, ", name) 

#print('hello ', end="")
#print(name)

#print(f"hello, {name}")


def hello(to="world"):
    print('hello,', to)

hello()
name = input ("What's your name? ")
hello(name)
