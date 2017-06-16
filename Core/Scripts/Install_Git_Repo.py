
print("\n" * 10)
print("Loading App\n")
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
alist = dir_path.split('Core')

Settings_File = open(alist[0] + 'Settings.txt')
List_Of_Lines_In_Settings_File = Settings_File.readlines()
for line in List_Of_Lines_In_Settings_File:
    exec(line)
if Repo_URL != None:
    git = alist[0] + 'Core\cmd\git.exe'
    gitProject = alist[0] + 'App'
    os.chdir(gitProject)
    command = git + ' clone ' + Repo_URL + " ."
    print(command)
    print('Please Wait For Finished...')
    os.system(command)
    print('Finished')
    
else:
    print("'Repo_URL' = None\n")
    print("You must set 'Repo_URL' in Settings.txt!")






