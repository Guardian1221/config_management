import os
def ls_command(realls):
    if realls == "ls":
        return os.listdir()
def cd_command(realcd):
    if realcd == "cd":
        return os.chdir()  
def exit_command(realexit):
    if realexit == "exit":
        return os.listdir()