def main():

    import random
    secret_number = random.randint(1, 10)

    number = int(input("What is your number? "))
    if secret_number == number:
        print("Yay you win")
    elif secret_number < number:
        print("Wrong, too high. it was " + str(secret_number))
    elif secret_number > number:
        print("Wrong, too low. it was " + str(secret_number))

main()