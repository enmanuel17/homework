#enmanuel hernandez
#program that rename a set of files to decrypt a secret message

import os

#defines a function that rename files.
def rename_files():
	#Get file names from a folder
	file_list = os.listdir(r"/home/enmanuel/Downloads/prank/prank")
	print (file_list)
	
	#To get the current working directory 
	saved_path = os.getcwd()
	print ("Current directory is "+saved_path)
	
	#changing directory to rename files properly
	os.chdir(r"/home/enmanuel/Downloads/prank/prank")
	#For each file, rename filename
	for file_name in file_list:
		print ("Old file name "+file_name)
		print ("New file name "+file_name.translate(None,"0123456789"))
		os.rename(file_name,file_name.translate(None,"0123456789"))
	#return to the old cwd
	os.chdir(saved_path)
	
#execute the function to start the program (main function)
rename_files()
