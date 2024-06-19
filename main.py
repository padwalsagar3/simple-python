# main.py
from helper import greet
from math import add, subtract
name = input("Enter the name: ").strip()

def main():
    print(greet(name))
    print("3 + 5 =", add(3, 5))
    print("10 - 4 =", subtract(10, 4))

if __name__ == "__main__":
    main()
