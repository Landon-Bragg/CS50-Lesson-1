#x = int(input("What is x? "))

#if x % 2 == 0:
  #  print("even")
#else:
 #   print("odd")

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
