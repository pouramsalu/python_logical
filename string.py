str="aaabbcccdd"
a=""
b=str[0]
count=0
for ch in str:
    if ch==b:
        count+=1
    else:
        a=a+str(count)+b
        count=1
        b=ch
a=a+str(count)+b
print(a)