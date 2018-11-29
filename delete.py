import os

g = os.walk("/home/username/python")
for path ,d ,filelist in g:
    for filename in filelist:
        if filename.endswith('jpg'):
            print ('deleting '+ (os.path.join(path,filename)) + '...')
            os.remove(os.path.join(path,filename))
