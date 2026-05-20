# nums={1,2,3,4,5}
# for val in nums:
#     print(val)
# str="pdeu"
# for char in str:
#     print(char)

lis= [1,4,9,16,25,36,49,64,81,100]
for val in lis:
    print(val)

list2= [1,4,9,16,25,36,49,64,36,81,100,36]
idx=0
for num in list2:
    if(num==36):
        print("Found the number at index ",idx)
    idx+=1
    
        