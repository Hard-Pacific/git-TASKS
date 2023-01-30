def simple(n):
    numbers = set(range(2, n+1))
    while numbers:
        prime = min(numbers)
        print(prime, end = "\t")
        numbers -= set(range(prime, n+1, prime))

if __name__ == "__main__":
    n = int(input("Введите число: "))
    simple(n)
