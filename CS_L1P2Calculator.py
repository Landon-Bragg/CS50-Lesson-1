#x = float(input("What is x? "))
#y = float(input('What is y? '))

#z = (x / y)

#print(f"{z:.2}")

def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    return n*n

main()