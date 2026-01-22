import math  

def main():
    sides = input("Please input the lengths of the two sides separated by a comma: ")
    A, B = map(float, sides.split(","))
    print(pythag(A, B))

def pythag(A,B):
    return math.hypot(A, B)

main()
