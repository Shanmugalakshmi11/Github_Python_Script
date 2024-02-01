def factorial(n):
    if n == 0 | n == 1:
        print(f"Reach Termination Condition")
        return 1
    else:
        print(f"Number: {n}")
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	
zahl = int(input("Enter the number:"))
result =factorial(zahl)
print(f"Factorial {zahl} and {result}")