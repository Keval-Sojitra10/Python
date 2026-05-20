num= int(input("Enter a value:"))
def calc_sum(a):
    if(a==0):
        return 0
    return calc_sum(a-1)+ a
sum = calc_sum(num)
print(sum)

list1= [1,2,3,"p","d","e","u"]
def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx],end=" ")
    print_list(list,idx+1)
print_list(list1,0)