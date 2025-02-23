import os

path='needed_format/data'
l=os.listdir(path)
l.sort()

for file in l:
    os.rename(os.path.join(path,file),os.path.join(path,'.'.join((file.split('_')[0],'txt'))))
