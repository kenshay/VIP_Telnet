print("Load App\n")
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
alist = dir_path.split('Core')
git = alist[0] + 'Core\cmd\git.exe'
gitProject = alist[0]
os.chdir(gitProject) 
os.system(git + ' reset --hard origin/master')
os.system(git + ' fetch --all')
os.system(git + ' reset --hard origin/master')
os.system(git + ' status')





