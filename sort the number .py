# list=[1,2,2,2,3,3,4,5,5,6,6]
# output//[1,4]

# list=[1,2,2,2,3,3,4,5,5,6,6]
# new_list=[]
# for num in list:
#     if list.count(num)==1:
#         new_list.append(num)
# print(new_list)

# OR

# list=[1,2,2,2,3,3,4,5,5,6,6]
# print([num for num in list if list.count(num)==1])

# write a sorting function without using the list.sort function(descending order)

# a=[24,55,78,64,25,12,22,11,1,2,44,3,122,23,34]
# b=[]
# while a:
#     minimum=a[0]
#     for x in a :
#         if x>minimum:
#             minimum=x
#     b.append(minimum)
#     a.remove(minimum)
# print(b)


# sorting the list and than print second last number:
num=[78,45,76,90,23,37,84]
num.sort()
print(num)
print("second last largest number is: ",num[-2])

