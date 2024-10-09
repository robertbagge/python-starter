from maths.add import add
from maths.multiply import multiply

if __name__ == "__main__":
    a = 2
    b = 3
    print(f"Starting with number {a} and {b}")
    added = add(a, b)
    print(f"Adding {a} and {b}")
    multiplied = multiply(added, 4)
    print("Multiplying by 4")
    print("Result is 42!")
