#i = 0
#while i  < 3 :
  #  print("meow")
   # i += 1

#for _ in range(3) :
   # print("meow")

#print("meow\n" * 3, end = "")

##Asking the user how many times to meow

#while True:
    #n = int(input("How many times should the cat meow? "))
    #if n > 0:
      #  break

#for _ in range(n):
    #print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        x = int(input("How many times does the cat meow? "))
        if x > 0:
            return x

def meow(n):
    for _ in range(n):
        print("meow")

main()
