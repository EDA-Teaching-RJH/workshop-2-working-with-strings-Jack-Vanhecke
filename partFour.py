def main():

    year = int(input("What is your age? "))
    print(myFunction(year))

def myFunction(age):
    if int(age) < 18:
        return "You are a child."
    else:
        return "You are an adult."

main()