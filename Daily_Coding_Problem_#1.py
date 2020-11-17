# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


# Solution:


import itertools
arr=list(map(int,input().split()))
total=int(input())
sets=list(itertools.combinations(arr,2))
new=[]
for i in sets:
    new.append(sum(i))
if total in new:
    indx=new.index(total)
    a=sets[indx]
    print(f"{a[0]} + {a[1]} = {total}")
    print("True")



# x=set()
# for i in arr:
#     if (total-i) in x:
#         print("True")
#         exit()
#     else:
#         x.add(i)
# print("False")


