def fib(n):  
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
def all_fib(n):  
    fibs = []
    for i in range(n):
        fibs.append(fib(i))
    return fibs
print("The first 10 fibbonaci series is : ")
print(all_fib(10))
