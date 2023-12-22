import sys

def factorize(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(f"{n}={i}*{n//i}")
            return

    # If no factorization found (prime number)
    print(f"{n} is a prime number")

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = int(line.strip())
                factorize(number)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid content in file '{file_path}'. All lines must contain valid natural numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
