def fun(n):
    if (n > 0):
        print(n, end=" ")
        # Last statement in the function
        fun(n - 1)
 
# Driver Code
x = int(input("enter number : ")) 
fun(x)
