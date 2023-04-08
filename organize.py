import os
import shutil 

fromDir = "C:/Users/chuja/Downloads"
toDir = "C:/Users/chuja/OneDrive/Desktop/imagess"

listOfFiles = os.listdir(fromDir)
print(listOfFiles)

for fileName in listOfFiles :
    name, extention = os.path.splitext(fileName)
    print(name)
    print(extention)


    if extention == '':
        continue
    if extention in ['.gif', '.jfif', '.jpg', '.jpeg', '.png']:
        path1 = fromDir + '/' + fileName
        path2 = toDir + "/" + 'images'
        path3 = toDir + "/" + 'images' + '/' + fileName

        print("path1", path1)
        print("path2", path2)
        print("path3", path3)
        if os.path.exists(path2):
            print("moving.." + fileName)
            shutil.move(path1, path3)

        else : 
            os.makedirs(path2)
            print("moving.." + fileName)
            shutil.move(path1, path3)
        

       

