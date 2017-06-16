
print("\n" * 10)
print("Loading App\n")
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
alist = dir_path.split('Core')

Settings_File = open(alist[0] + 'Settings.txt')
List_Of_Lines_In_Settings_File = Settings_File.readlines()
for line in List_Of_Lines_In_Settings_File:
    exec(line)


dir_path = os.path.dirname(os.path.realpath(__file__))
alist = dir_path.split('Core')
git = alist[0] + 'Core\cmd\git.exe'
gitProject = alist[0]
os.chdir(gitProject) 
os.system(git + ' config --global user.email ' + userEmail)
os.system(git + ' config --global user.name ' + name)







