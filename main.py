# Accept user input

getvalue = (input("Enter a number between 1,3 and 5 to proceed \n"))

# Match input against values 1,3,5 to verify identity
while getvalue != "1" and getvalue != "3" and getvalue != "5":
    print("You are a taliban")
    exit()

    # If input is correct display text
else:
    def main():

        f = open("reader.txt", "r")

        content = f.readlines()

        for x in content:
            print(x)

        f.close()


    if __name__ == "__main__":
        main()

