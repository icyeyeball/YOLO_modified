import os
yourPath = '../../peitent/crawler/yoloin2/'
allFileList = os.listdir(yourPath)
#print(allFileList)
for file in allFileList:
    if 'M' in file[0]:
        print(file)

