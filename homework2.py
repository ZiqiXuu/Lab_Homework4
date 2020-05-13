import os
import string
def q1(file):
    list1=[]
    for arg,dirname,name in os.walk(file):
      for i in name:
        if i[-3:-1]=='mp3':
          list1.append(arg+'/'+i)
    return list1
def q2(file1,file2):
  if os.path.samefile(file1, file2)==True:
    return True
  else return False
