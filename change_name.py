##changing images name in folder:
import os
os.chdir('C:\\Users\\blabla\\OneDrive\\Desktop\\blackhole') ##location of folder
i=0
for file in os.listdir():
      src=file
      dst="frame"+str(i)+".jpg"
      os.rename(src,dst)
      i+=1