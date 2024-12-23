# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.

import os        #for file and folder operations
import shutil       #for moving, copying and organizing files and folders
import glob     #for finding files using patterns
import keyboard

class organizeFiles:

 
 
 def on_key_y(self):
  print("press Y to confirm, N to cancel:")
  choice = input().strip().lower()
  return choice == 'y'
  
 def fileOrganize(self):
  print(" ")
  print("First, please let me know what folder path you want to use to organize: ")
  
  path = input("folder path, please insert:")
  ifExists = os.path.isdir(path)
  if ifExists:
    print("path exists")   # this  is not checked lol.
  else:
    print('this directory does not exist, try again, also try putting / symbol infront ')
    print("Try again. ")
    path = input("folder path, please insert:")
    ifExists = os.path.isdir(path)  
    if ifExists:
     print("path exists")
    else:
     print('Sorry, you made a mistake again., Try once again.')
     self.fileOrganize()
    
  #print("do you want to loop through the folder and find files by format?")  
  for files in os.listdir(path):
   root, extension = os.path.splitext(files)
   print(root + " and " + extension)
   print("do you want to create a folder for this extension? choose Yes or No")
   #inp = input()
   
   if self.on_key_y():
    print("do you want to choose a new folder directory for this new folder? Y/N")
    
    if self.on_key_y():
     path = input("insert the new path")
    else: 
     print("the folder will be created in currently selected folder.")
    
    print("choose the name for your new " + extension +  " file directory.")
    newfolder = input("choose: ")
    newpath = path + "/" + newfolder
    os.mkdir(newpath)
    print(newpath) 
    for i in os.listdir(path):
     
     roots, extensions = os.path.splitext(i)
     if extensions == extension:
      filepath = path + '/' + i
      shutil.move(filepath, newpath)
   
   else:
    print("app is closing")
     

 def moveFile(self):                       #HAS TO ALSO DETECT THE FILE,    
  print("insert directory of a file or folder you want to move: ")
  path = input(":")
  print(" ")
  checkIfFile = os.path.isfile(path) 
  ifExists = os.path.isdir(path)
  if checkIfFile or ifExists:
   print(" ")
  else:
   print('Sorry, file/folder doesnt exist, Try once again.')
   self.moveFile()
   
  print("choose folder directory you want to move the file/folder to:") 
  newpath = input(':') 
  ifExists = os.path.isdir(newpath)  
  if ifExists:
   print("path exists")
   shutil.move(path, newpath)
   print("file/folder is moved to the new directory folder.")
   start()
   
  else:
   print("directory doesn't exist. try it all again.'")
   print("choose folder directory you want to move the file/folder to:") 
  newpath = input(':') 
  ifExists = os.path.isdir(newpath)  
  if ifExists:
   print("path exists")
   shutil.move(path, newpath)
   print("file/folder is moved to the new directory folder.")
   start()
  else:
   print("directory doesn't exist. try it all again.'")
   self.moveFile()
   

 def FindF(self):
  path = input("insert a folder of the file where I should find it:")
  file = input("insert the name of a file, or a part name, you want to find:")
  ifExists = os.path.isdir(path)
  if ifExists:
   print("path exists")
  else:
   print("directory doesn't exist. try it all again.'")
   self.FindF()
  filepath = path + '/' + file 
  input2 = os.path.isfile(filepath) 
  if input2:
     print(input2)
     print("file exists in this folder")
  else:
   print("file does not exist in this folder.")
  print(" ")
  repeat = input("you want to find another file? Y/N")
  if repeat == "y":
   self.FindF()
  else:
   start() 
  
  
def start(): 
 
 obj = organizeFiles()

 print("please choose what you would like to do?")
 print("choose if you want:")
 print("organize your files according to their format (f.e. .txt) and put them in newly created folders PRESS '1' ?")
 print("or just move files/folders from one directory to another PRESS '2'? ")
 print("you want to find a certain file by name in a certain folder? PRESS '3'")
 print(" ")
 input1 = input()    
 if input1 == '1':
  obj.fileOrganize()
 
 if input1 == '2':
  obj.moveFile()  
 
 if input1 == '3':
  obj.FindF()   
  

start()  
