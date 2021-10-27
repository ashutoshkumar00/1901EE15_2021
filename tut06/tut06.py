import os
import re
import shutil

os.system('cls') 
if(os.path.isdir(r'.\correct_srt')):
      pass
else:      
    os.makedirs('.\correct_srt')


def rename_Breaking_Bad(season_padding,episode_padding):

    if(os.path.isdir(r'.\correct_srt\Breaking Bad')):
        shutil.rmtree('.\correct_srt\Breaking Bad')
    
    shutil.copytree(r".\wrong_srt\Breaking Bad",r".\correct_srt\Breaking Bad",symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

    path=r".\correct_srt\Breaking Bad"

    for filename in os.listdir(path):

        lis=re.split('\s',filename)
        sno=int(lis[2][1:lis[2].index('e')])
        eno=int(lis[2][lis[2].index('e')+1:])
        sno=str(sno)
        eno=str(eno)

        while len(sno)<season_padding:
            sno='0'+sno
        
        while len(eno)<episode_padding:
            eno='0'+eno
        
        extension=''

        ext=re.search(r".srt$",filename)

        if ext:
            extension=".srt"
        else:
            extension=".mp4"

        os.rename(path+'/'+filename, path+'/' +lis[0]+' '+ lis[1]+' - Season '+sno+' Episode '+eno+extension)


def rename_Game_Of_Thrones(season_padding,episode_padding):

    if(os.path.isdir(r'.\correct_srt\Game of Thrones')):
        shutil.rmtree('.\correct_srt\Game of Thrones')
    
    shutil.copytree(r".\wrong_srt\Game of Thrones",r".\correct_srt\Game of Thrones",symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

    path=r".\correct_srt\Game of Thrones"

    for filename in os.listdir(path):

        lis=re.split(' - ',filename)
        sno=int(lis[1][0:lis[1].index('x')])
        eno=int(lis[1][lis[1].index('x')+1:])
        ename=lis[2][0:lis[2].index('.')]
        sno=str(sno)
        eno=str(eno)

        while len(sno)<season_padding:
            sno='0'+sno
        
        while len(eno)<episode_padding:
            eno='0'+eno
        
        extension=''

        ext=re.search(r".srt$",filename)

        if ext:
            extension=".srt"
        else:
            extension=".mp4"

        os.rename(path+'/'+filename, path+'/' +lis[0]+' - Season '+sno+' Episode '+eno+' - '+ename+extension)

def rename_Lucifer(season_padding,episode_padding):

    if(os.path.isdir(r'.\correct_srt\Lucifer')):
        shutil.rmtree('.\correct_srt\Lucifer')
    
    shutil.copytree(r".\wrong_srt\Lucifer",r".\correct_srt\Lucifer",symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

    path=r".\correct_srt\Lucifer"

    for filename in os.listdir(path):

        lis=re.split(' - ',filename)
        sno=int(lis[1][0:lis[1].index('x')])
        eno=int(lis[1][lis[1].index('x')+1:])
        ename=lis[2][0:lis[2].index('.')]
        sno=str(sno)
        eno=str(eno)

        while len(sno)<season_padding:
            sno='0'+sno
        
        while len(eno)<episode_padding:
            eno='0'+eno
        
        extension=''

        ext=re.search(r".srt$",filename)

        if ext:
            extension=".srt"
        else:
            extension=".mp4"

        os.rename(path+'/'+filename, path+'/' +lis[0]+' - Season '+sno+' Episode '+eno+' - '+ename+extension)


def regex_renamer():

    print("1. Breaking bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num=int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    if(webseries_num==1):
        rename_Breaking_Bad(season_padding,episode_padding)

    elif(webseries_num==2):
        rename_Game_Of_Thrones(season_padding,episode_padding)
    
    elif(webseries_num==3):
        rename_Lucifer(season_padding,episode_padding)

    else:
        print("Try again")
        regex_renamer()      
regex_renamer()       