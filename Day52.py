def SieveOfEratosthenes(n):
    primes = [True] * (n + 1)  # Initialize all entries as True
    p = 2  # The smallest prime number

    while (p * p <= n):
        # If primes[p] is still True, then it's a prime
        if primes[p] == True:
            # Marking all multiples of p as False
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1

    # Printing all prime numbers
    for i in range(2, n):
        if primes[i]:
            print(i)

if __name__ == "__main__":
    n = int(input("Enter a number to check all smaller prime numbers: "))
    SieveOfEratosthenes(n)
