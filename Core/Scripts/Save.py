print("Load App\n")
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
alist = dir_path.split('Core')
git = alist[0] + 'Core\cmd\git.exe'
gitProject = alist[0]
os.chdir(gitProject) 
os.system(git + ' add --all')
os.system(git + ' commit -a -m "auto"')
os.system(git + ' push')
os.system(git + ' status')





