# second highest number in a list using for loop

def second_highest_number(n):
    if n[0]>n[1]:
        first=n[0]
    else:
        first=n[1]
        second=n[0]
    for i in range(2,len(n)):
        if n[i]>first:
            second=first
            first=n[i]
        elif n[i]>second and first !=n[i]:
            second=n[i]
        return second
n=[10,20,30,4,100,22,666,666]
print(second_highest_number(n))


# using set and max

# a=[10,20,30,4,100,22,666,666]
# b=set(a)
# print(b)
# b.remove(max(b))
# print(b)
# print(max(b))
        