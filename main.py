# main.py
from helper import greet
from math_operations import add, subtract

def main():
    print(greet("Alice"))
    print("3 + 5 =", add(3, 5))
    print("10 - 4 =", subtract(10, 4))

if __name__ == "__main__":
    main()
