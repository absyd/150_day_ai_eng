# optimal solution using ai 

# Given an integer array of size n, find all elements that appear more than ⌊n/3⌋ times.

arr =[1,1,1,1,1,1,3,4,5,5,6,7,8]
n=len(arr)
target_num=int(n/3)

num_dict={}

for num in arr:
     num_dict[num]=num_dict.get(num,0)+1
     
     
     
print(num_dict)
print(list(num_dict))

num_appers_than_3=[]
for num in list(num_dict):
    if(num_dict[num]>3):
        num_appers_than_3.append(num)
    


# print(num_appers_than_3)
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

num =5554845
k=2

new_num=str(num)
new_num=new_num[2:]

new_num_len=len(new_num)
new_num_int=int(new_num)


print(int(new_num_int/int("1"+"0"*(new_num_len-1))))