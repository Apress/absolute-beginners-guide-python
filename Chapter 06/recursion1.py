def factorial(n):
    if n <= 1:
        return 1
    else:
        f = factorial(n-1)
        a = f * n
        print (f, "x", n, "=", a)
        return a


print("\nFactorial of 7 is", factorial(7))
