n  = int(input("Enter a number"))
isPrime = 0
for i in range(2,n):
    if n%i == 0:
        break
    else:
        isPrime = 1

if (isPrime == 1):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
