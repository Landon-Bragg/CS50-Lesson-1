def main():
    print_square(3)

def print_square(size):

    #for each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            #Print brick
            print("#", end="")
        print()

main()


