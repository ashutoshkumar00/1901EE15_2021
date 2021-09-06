import os
import os.path
os.system("cls")

def output_by_subject(csvFile):
     folder = "output_by_subject"
     if os.path.exists(folder)==False:
        os.makedirs(folder)

     with open(csvFile,'r') as f:
         main_line=""

         for line in f:
            newlist=line.split(',')

            if(newlist[0]=="rollno"):
                tophead =[newlist[0],newlist[1],newlist[3],newlist[8]]

                for word in tophead:
                    main_line+=word+","
                main_line=main_line[:-1]
                
            else :
                new_line=""
                listdatas =[newlist[0],newlist[1],newlist[3],newlist[8]]

                for word in listdatas:
                    new_line+=word
                    new_line+=","
                new_line=new_line[:-1]

                course = os.path.join(folder, listdatas[2]+".csv")  
                if os.path.isfile(course):
                        roll_file=open(course,'a')
                        roll_file.write(new_line)
                        roll_file.close()
                else:  
                        roll_file=open(course,'w')
                        roll_file.write(main_line)
                        roll_file.write(new_line)
                        roll_file.close()
     return
 
def output_individual_roll(csvFile):
    folder = "output_individual_rol"
    if os.path.exists(folder)==False:
        os.makedirs(folder)

    with open(csvFile,'r') as f:
         main_line=""

         for line in f:
            newlist=line.split(',')

            if(newlist[0]=="rollno"):
                tophead =[newlist[0],newlist[1],newlist[3],newlist[8]]

                for word in tophead:
                    main_line+=word+","
                main_line=main_line[:-1]
                
            else :
                new_line=""
                listdatas =[newlist[0],newlist[1],newlist[3],newlist[8]]

                for word in listdatas:
                    new_line+=word
                    new_line+=","
                new_line=new_line[:-1]

                course = os.path.join(folder, listdatas[0]+".csv")  
                if os.path.isfile(course):
                        roll_file=open(course,'a')
                        roll_file.write(new_line)
                        roll_file.close()
                else:  
                        roll_file=open(course,'w')
                        roll_file.write(main_line)
                        roll_file.write(new_line)
                        roll_file.close()
    return




csvFile="regtable_old.csv"
output_individual_roll(csvFile)
output_by_subject(csvFile)







