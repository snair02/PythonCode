import os;
def rename_file():
    #list the files in directory
    file_list=os.listdir("/Users/snehanair/Documents/Onlinecourse/prank");
    print(file_list)
    os.chdir("/Users/snehanair/Documents/Onlinecourse/prank")
    #rename files
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,'0123456789'))

rename_file()
