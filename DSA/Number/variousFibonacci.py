def fibonacci(num):
    if num == 0:
        return [0]
    elif num == 1:
        return [0,1]
    else:
        fib = [0,1]
        i = 1
        while i < num:
            fib.append(fib[-1] + fib[-2])
            i += 1
        return fib 
n = int(input("Enter a number: "))
print(f'All {n} Fibonacci numbers are: {fibonacci(n)}')