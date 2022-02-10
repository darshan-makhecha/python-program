def all_fib_dp(n):  
    fibs = []
    for i in range(n):
        if i < 2:
            fibs.append(i)
        else:
            fibs.append(fibs[i - 2] + fibs[i - 1])
    return fibs
print(all_fib_dp(40))
