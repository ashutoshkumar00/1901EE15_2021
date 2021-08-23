def get_memory_score(input_nums):
    total_score_of_game=0
    memory_score=[]
    
    for score in input_nums:
        
        if(score in memory_score):
            total_score_of_game+=1
            
        else:
            
            if(len(memory_score)==5):
                memory_score.pop(0)
            memory_score.append(score)    
            
            
     
     
    return   total_score_of_game      




input_nums =  [3, 4, 5, 3, 2, 1]

non_int_present=[]

for val in input_nums:
    if(isinstance(val,int)==False):
        non_int_present.append(val)
        
        
if(len(non_int_present)==0):
    
    print("Score:",get_memory_score(input_nums))
    
else:
    print("Please enter a valid input list. Invalid inputs detected: {}".format(non_int_present))
    