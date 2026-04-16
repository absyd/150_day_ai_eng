


# =========== ==Given an integer N, find all the divisors of N.================

# ai. baba ai 
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(find_divisors(12))

# =========== ==Given an integer N, find all the divisors of N.================

# =========== Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

def find_divisor(n):
    if n ==0:
        return None
    else:
        for i in range(1,n+1):
            if n%i==0:
                print(i)
                
                
                
find_divisor(9)

def divisors(n):
    result=set()
    
    if n==0:
        return None
    
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            result.add(i)
            result.add(n//i)
            print(i,"n//i : ",n//i)
            
    return result
    
print(divisors(9))

# =========== Given two sorted arrays A and B, combine all the elements of A and B into a new sorted array C.  .================

arr1=[1,2,3,4,5]
arr2=[1,2,3,4,5]

new_arr=sorted(arr1+arr2)

print(new_arr)


def merge_sorted_array(arr1,arr2):
    i,j=0,0
    C=[]
    
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            C.append(arr1[i])
            i+=1
        else:
            C.append(arr2[j])
            j+=1
            
    while i<len(arr1):
        C.append(arr1[i])
        i+=1
        
    while j<len(arr2):
        C.append(arr2[j])
        j+=1
        
    return C
    


print(merge_sorted_array(arr1,arr2))