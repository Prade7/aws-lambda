
# n=int(input())
# for i in range(n+1):
#     for j in range(n-i):
#         print("",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# n-=1
# for i in range(n):
#     for j in range(i+1):
#         print("",end=" ")
#     for k in range(n-i):
#         print("*",end=" ")
#     print()

# n=65
# for i in range(5):
#     for j in range(i+1):
#         print(chr(n),end=" ")
#     print()
#     n+=1


# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()


#     1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1

# n=5
# res=[]
# for i in range(n):
#     temp=[]
#     for j in range(i+1):
#         if(j==0 or j==i):
#             temp.append(1)
#         else:
#             temp.append(res[i-1][j-1]+res[i-1][j])
#     res.append(temp)
# print(res)


                ### floyd triangle
                
# n=5
# c=1
# for i in range(n):
#     for j in range(i):
#         print(c,end=" ")
#         c+=1
#     print()


            ### full pyramid
            
# n=5

# result=[]
# for  i in range(n):
#     temp=[]
#     for j in range(i+1):
#         if(j==0 or j==i):
#             temp.append(i)
#         else:
#             temp.append(result[i-1][j-1]+result[i-1][j])
#     result.append(temp)
# print(result)

            ###printing odd stars
# n=5
# for i in range(n+1):
#     for j in range(i+1):
#         print("*",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()
        

# def merge_sort(arr):
#     if(len(arr)>1):
#         left=arr[:len(arr)//2]
#         right=arr[len(arr)//2:]
#         merge_sort(left)
#         merge_sort(right)
#         i=0
#         j=0
#         k=0
        
#         while(i<len(left) and j<len(right)):
#             if(left[i]<right[j]):
#                 arr[k]=left[i]
#                 i+=1
                
#             else:
#                 arr[k]=right[j]
#                 j+=1
#             k+=1
        
#         while(i<len(left)):
#             arr[k]=left[i]
#             i+=1
#             k+=1
#         while(j<len(right)):
#             arr[k]=right[j]
#             j+=1
#             k+=1
#     return arr
# print(merge_sort([8,6,4,3,2,9]))


# inp=input().split(" ")
# inp=list("".join((inp)))
# nums=[]
# for i in inp:
#     nums.append(int(i))
# print(merge_sort(nums))

# nums=[1,2,3,4,5,6]
# target=-6
# low=0
# high=len(nums)-1

# while(low<=high):
#     mid=(low+high)//2
#     print("hi")
#     if(nums[mid]==target):
#         print(mid)
#         break
    
#     if(nums[mid]<target):
#         low=mid+1
#         print("left")
#     elif(nums[mid]>target):
#         high=mid-1
#         print("right")
    # break


# d=[1,9,8,6,5,5,5,9,9,8,5]

# hm={}

# for ele in d:
#     if(ele not in hm):
#         hm[ele]=1
#     else:
#         hm[ele]+=1
# print(hm)

# import Counter
# cnt = Counter(arr)      # Use Counter() to get numbers and their frequency
# num_freq = sorted(cnt.values(), reverse=True)


# l1=["name 1 label","name 2 label","name 3 label"]

# a=int(input())
# nums=[]
# for i in range(a):
#     inp1=input().split()
#     n=[int(inp1[0]),int(inp1[1])]
#     nums.append(n)
# count=0
# for ele in nums:
#     if((ele[0])%2==0 and ele[1]%2==0):
#         count+=1
        
#     if(count==4):
#         print(0)
#         break
# if(count<4):
#     print(4-count)


# class fruits():
#     def __init__(self):
#         book="harry potter"
#         print(book)
#         # pass
# apple=fruits()
# mango=fruits()
# apple



# a=(1,1,3,4,5,9,2,6,3,2,4,4,2,1,1,1,2,1,1,2,3,1,2,3)
# print(a)


# res = []
# nums.sort()

# for i, a in enumerate(nums):
#     if i > 0 and a == nums[i - 1]:
#         continue

#     l, r = i + 1, len(nums) - 1
#     while l < r:
#         threeSum = a + nums[l] + nums[r]
#         if threeSum > 0:
#             r -= 1
#         elif threeSum < 0:
#             l += 1
#         else:
#             res.append([a, nums[l], nums[r]])
#             l += 1
#             while nums[l] == nums[l - 1] and l < r:
#                 l += 1
#     return res


# n=input()
# l1=[int(i) for i in input().split()]
# print(l1)

# for i in range(5):
#     inp=input()
# i=input()
# print("hii")

# nik=input()
# thenn=input()
# nik=list(nik)
# thenn=list(thenn)
# for ele in nik:
#     if(ele in thenn):
#         nik.remove(ele)
# print(nik)



# thenn=int(input())
# n=int(input())
# arr=[int(i) for i in range(input().split())]

# def getPairs(arr,n,thenn):
#     count=0
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if(arr[i]+arr[j]==thenn):
#                 count+=1
#     return count
# getPairs(arr,n,thenn)


# nk1=input()
# nk2=input()
# arr=[]
# string=""
# list1=[]
# for i in nk1:
#     list1.append(i)
# for i in nk2:
#     if(i in list1):
#         c=list1.count(i)
#         for j in range(c):
#             list1.remove(i)
# for i in list1:
#     string+=i
# print(string)


# a,b=list(map(int,input().split()))

# print(a)
# print(b)

# thenn,nikk=list(map(int,input().split()))
# cap=0
# mm,nn=0,0
# for h in range(thenn):
#     z=[int(k) for k in input()]
#     for d in range(len(z)-1):
#         if(z[d]==1 and z[d+1]==1):
#             mm+=2
#             z[d],z[d+1]=0,0
#     cap+=(z.count(1))
# b=0
# while(cap!=0):
#     if(b%2==0):
#         nn+=1
#     else:
#         mm+=1
#     b+=1
#     cap-=1
# print(nn)




# a=int(input())
# b=list(input().split())
# c=0
# m,n=0,0
# for h in range(a):
#     z=[int(k) for k in input()]
#     for d in range(len(z)-1):
#         if z[d]==1 and z[d+1]==1:
#             m+=2
#             z[d],z[d+1]=0,0
#     c+=(z.count(1))
# b=0
# while c!=0:
#     if b%2==0:
#         n+=1
#     else:
#         m+=1
#     b+=1
#     c-=1
# print(n)

# print(91%3)




# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.


# num1=list(int(i) for i in input())
# num2=list(int(j) for j in input())



# num1=(input())
# array1=[]
# for ele in (num1):
#     array1.append(int(ele))
# print(array1)
# num2=input()
# array2=[]
# num2=input()
# for ele in num2:
#     array2.append(int(ele))
# print(array2)

# from array import array


# list1=[0,4,6,8]
# list2=[0,1,4,6,8,9]



# list1[len(list1):]=list2[::]
# print(list1)


# print(list1)

# list1.sort()
# for ele in list1:
#     if(ele==0):
#         list1.remove(ele)
#     else:
#         break
# print(list1)



# array
# two pointers
# binary search ,sorting
# hash table


# list1=[8,6,5,4,3,1]
# i=0
# l=len(list1)-1

# while()

# a=6
# for i in range(a):
#     print(i)


# if(len(list2)>=len(list1)):
#     for ele in range(len(list1)):
        
# s="byubkyby"
# k=2
# a=list(s)
# for i in range(0,len(a),2*k):
    # a[i:i+k]=a[i:i+k][::-1]
    # print(i)
        # return("".join(a))
        
        

# list1=[1,3,6,8,9]

# list2=[2,5,6,7,9,10]

# i=len(list1)-1
# j=len(list2)-1
# k=j
# list3=[]
# for ele in range(len(list2)):
#     if(i<j):
#         list3.append()
        
# for ele in range(len(j)):
#     if(ele<=len(list1)):
#         if(list1[ele]<)

# m=6
# n=30
# e=0
# for ele in range(1,n+1):
#     if(ele%m!=0):
#          e+=ele
#          print(ele)
# print(e)

# inp1=eval(input())
# print(inp1)


# s="NIK"
# s=s.index("z")
# print(s)

# a=9
# a=9.9
# a=""
# a=[]
# a=True
# a=False
# a=()    #tuple
# a={"p","n","p"}      #set
# # a={"a":9}
# print(a)


# a="nikk"
# print(a.rfind("k"))

# a=[1,2,3,4,"prd",8.5]
# a.append("thenn")
# a.append(8)
# print(a)
# fruits = ['apple', 'banana', 'cherry']

# # fruits.pop()
# print(fruits)

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# a="nikhalyaa"
# print(a[::5])


# for i in range(0,5,2):
#     print(i)

# while(True):
#     print("nikk")




# a=["theschool","nikk"]

# for ele in a:
#     print(ele)


# n=5
# for i in range(n):
#     print(i)


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n-i):
#         print("*",end=" ")
#     print()


# i=1
# while(i<30):
#     print("bgbg")
#     i+=1
#     if i==6:
#         break
# else:
#     print("vrevtbvrt")

# for i in range(6):
#     if(i==3):
#         # break
#         pass
# else:
#     print("nhtnhbn")

# N=5
# from collections import Counter
# c=Counter([int(i) for i in str(N)])

# print(c)

# n=563462346
# n1 = sorted(str(n))
# print(n1)

# n=5

# print(n*(n+1)//2)


# tar=7
# arr=[1,3,4,5,7,8]

# i=0
# l=len(arr)-1

# for i in range(len(arr)):
#     if(arr[i])


# hm={}
# nums=[1,2,3,5,6,7]
# target=9
# for i in range(len(nums)):
#     res=target-nums[i]
#     if(res in hm):    
#         print(i,hm[res])
#         break
#     hm[i]=res
# print(hm)

# if(8 in hm):
#     print(True)



# a=[1,2]
# b=[1,2]
# c=a
# print(a is b)
# print(a is c)


# nums=[1,2,3,0,0,0,2,5,6]
# def merge(nums):
#     if(len(nums)>1):
#         left=nums[:len(nums)//2]
#         right=nums[len(nums)//2:]
#         merge(left)
#         merge(right)
#         i=0
#         j=0
#         k=0
        
#         while(i<len(left) and j<len(right)):
#             if(left[i]<right[j]):
#                 nums[k]=left[i]
#                 i+=1
#                 k+=1
#             else:
#                 nums[k]=right[j]
#                 j+=1
#                 k+=1
#         while(i<len(left)):
#             nums[k]=left[i]
#             i+=1
#             k+=1
#         while(j<len(right)):
#             nums[k]=right[j]
#             j+=1
#             k+=1
#         return nums
# print(merge(nums))


# nums=[0,9,8,7,6,5,4,3]
# def merge(nums):
#     if(len(nums)>1):
#         left=nums[:len(nums)//2]
#         right=nums[len(nums)//2:]
        
#         merge(left)
#         merge(right)

#         i=0
#         j=0
#         k=0
        
#         while(i<len(left) and j<len(right)):
#             if(left[i]<right[j]):
#                nums[k]=left[i]
#                i+=1
#                k+=1
#             else:
#                 nums[k]=right[j]
#                 j+=1
#                 k+=1
#         while(i<len(left)):
#             nums[k]=left[i]
#             i+=1
#             k+=1
#         while(j<len(right)):
#             nums[k]=right[j]
#             j+=1
#             k+=1
#         return nums
# print(merge(nums))  



# nums=[1,2,3,4,6,7,8,9,10]
# target=5
# def binary(nums,target):
#     start=0
#     end=len(nums)-1
#     while(start<=end):
#         mid=(start+end)//2
        
#         if(nums[mid]==target):
#             return mid
#         elif(nums[mid]<target):
#             start=mid+1
#         else:
#             end=mid-1
#     return end
# print(binary(nums,target))


import csv

import json

# class CsvToJson(fileName):
#     def readCsv(self,fileName):
#         first_line_count=0
#         with open(filename,'r') as data:
#             result=[]
#             for line in  csv.reader(data):
#                 if(first_line_count==0):
#                     column={}
#                     first_line=line
#                     length_of_first_line=len(first_line)
#                     first_line_count+=1
#                     continue
                
#                 for i in range(length_of_first_line):
#                     if(line[i]!=""):
#                         column[length_of_first_line[i]]=line[i]
#                     result.append(column)
#                     column={}
        
        
   
    
    

# import csv
# import json
#    
# filename="/content/MOCK_DATA.csv"
# c=0
# with open(filename,'r') as data:
#   result=[]
#   for line in csv.reader(data):
#     if(c==0):
#       col={}
#       l=line
#       length=len(line)
#       c+=1
#       continue
#     for i in range(length):
#       col[l[i]]=line[i]
#     print(col)

# for key,value in json.items:
#     print(key,value)


import pyautogui
import time


time.sleep(5)
count=0
while(count<10):
    pyautogui.typewrite("Thenn")
    pyautogui.press("enter")
    count+=1

