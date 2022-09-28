# # fizzbuzz problem bu using for loop
# def fizzbuzz(n):
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             print("fizzbuzz")
#         elif i%3==0:
#             print("fizz")
#         elif i%5==0:
#             print("buzz")
#         else:
#             print(i)
# fizzbuzz(20)

# fizzbuzz by using for loop ,using dictionary
def fizzbuzz(n):
    d={3:"fizz",
       5:"buzz"}
    for i in range (1,n+1):
        a=" "
        for k,v in d.items():
            if i%k==0:
                a+=v
        if not a:
            a=i
        print(a)
fizzbuzz(15)