def meraki_helper(n):
    """This will detect meraki number"""
    """ASHUTOSH KUMAR 1901EE15"""
   
    string=str(n)
    
    for curr_ind in range(len(string)-1):
        curr_int=int(string[curr_ind])
        next_int=int(string[curr_ind+1])
        if(abs(curr_int-next_int)==1):
            continue
        else:
            print("No - {} is not a Meraki number".format(n))
            return False
    print("Yes - {} is a Meraki number".format(n))
    return True

input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
count_of_meraki=0
count_of_nonmeraki=0
for i in input:
    if(meraki_helper(i)):
       count_of_meraki+=1 
    else:
        count_of_nonmeraki+=1
print("the input list contains {} meraki and {} non meraki numbers".format(count_of_meraki,count_of_nonmeraki))