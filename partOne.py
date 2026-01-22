def main():
    slow = input("Please input text.")
    print(myFunction(slow))

def myFunction(text):
    new = text.replace(" ", "...")
    return(new)
    
main()
