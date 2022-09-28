# find the fibonnaci series from 0 to nth number using while loop
# 0 1 1 2 3 5 8 13 21 34

def fibonnaci(n):
    a,b=0,1
    print(a)
    while (b<n):
        print(b)
        a,b=b,a+b
fibonnaci(50)

# by using for loop
# def fibonnaci(n):
#     a,b=0,1
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# fibonnaci(50)

# by using recursion

# def fibonnaci(n):
#     if n<=1:
#         return n
#     else:
#         return(fibonnaci(n-1)+fibonnaci(n-2))
# n=10
# if n<=0:
#     print("invalid")
# else:
#     for i in range(n):
#         print(fibonnaci(i))

