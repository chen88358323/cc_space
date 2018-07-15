#-*-encoding:utf-8-*-
import os,sys

from  CountFile import CountFile
reload(sys)
sys.setdefaultencoding('utf-8')
import shutil
import hashlib


def mergeTargetDirInList(file_dir,dirList):
    for root, dirs, files in os.walk(file_dir):

        dirname=str(os.path.basename(root))
        if (dirname in dirList):

            mergeDir=createMergeDir(file_dir)
            dirname=file_dir+dirname+"/"
            print ('dirname :' + dirname)

            fileList=os.listdir(dirname)
            for file in fileList:
                if(not os.path.isdir(file)):
                    cutFile(dirname+file,mergeDir)

    # else:
    #     print (dirs + "is not targetDir ,ignore")

def printAllFile(file_dir):
    fileList=[]
    hashLikst=[]
    dirList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 过滤系统文件
    filterList = ['.DS_Store']
    list=os.listdir(file_dir)

    if ( os.path.isdir(file_dir)):
        mergeTargetDirInList(file_dir,dirList)


    else:
        print ("file:"+file_dir+"   is  not a  direction")

    for line in list:
        file = os.path.join(dir, line)

        if(not os.path.isdir(file)):
            # 截取文件名
            file = str(os.path.basename(file))

            if(file in filterList ):
                continue
            else:


                dirstr = getHashNum(file)  # 获取分片数

                createShardingDir(dirstr)

                cutFile(file, dirstr)

                fileList.append(file)

                hashLikst.append(dirstr)



    # for root, dirs, files in os.walk(file_dir):
    #     print(root)  # 当前目录路径
    #     print(dirs)  # 当前路径下所有子目录
    #     for file  in files:
    #
    #         #过滤系统文件
    #         list = ['.DS_Store']
    #
    #         if (file in list):
    #             continue
    #         dirFo=str(os.path.basename(root))
    #         if( dirFo in dirList):
    #             continue
    #
    #
    #         dirstr=getHashNum(file)#获取分片数
    #
    #         createShardingDir(dirstr)
    #
    #         cutFile(file,dirstr)
    #
    #         fileList.append(file)
    #
    #         hashLikst.append(dirstr)


            #print(files)  # 当前路径下所有非目录子文件

def filterSystemFile(str):
    list=['.DS_Store']
    if (str in list):
        return  true
    else:
        return false

#根据文件名 获取分位值
def getHashNum(fileName):
    # hashval = str(hash(fileName))

    hashval= hashlib.sha1(fileName).hexdigest()

    num = hashval[-2:-1]
    if (not num.isdigit()):
        num=str(ord(num))[-1]
    print ("name:"+fileName+"      hashcode:"+hashval+"     num:"+num)

    return  num;

#根据分片数建立文件夹
def createMergeDir(dirPath):
    if(os.path.isdir(dirPath)):
        dirPath=dirPath+"merge/"
        if (not os.path.exists(dirPath)):
            print ("create " + dirPath)
            os.mkdir(dirPath)
        else:
            print (dirPath + "has create")

        return dirPath;
    else:
        print ('create dir is fail ,target '+dirPath+" is not a direction")
        return ''


def cutFile(file,mergeDir):
    try:
        print ("src  =>"+str(file))
        print ("tarDir  =>"+mergeDir)
        shutil.move(str(file),mergeDir)
    except OSError,errormsg:
        print'fi exist!',errormsg


# dir="/home/cc/share/tt/cc/y"
#dir='W://w'


dir='/Users/chen.cc/Downloads/tmp/ll/'
countFile = CountFile(dir)
start = countFile.run()
printAllFile(dir.decode('utf-8'))
countFile = CountFile('/Users/chen.cc/Downloads/tmp/ll/merge/')
end = countFile.run()
print ("split file start:"+str(start)+"   end:"+str(end))



#old
#dir='F://迅雷下载'.decode('utf-8')
#myfile = open('list.txt','w')
#listdir(dir,myfile)
#myfile.close()

