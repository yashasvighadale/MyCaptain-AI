#fibonacci function definition
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#prints the series
for num in range(1,20):
    print(fib(num))
