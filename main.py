#-*-encoding:utf-8-*-
import os,sys

from  CountFile import CountFile
reload(sys)
sys.setdefaultencoding('utf-8')
import shutil
import hashlib
# def listdir(dir,file):
#     #print dir
#     file.write(dir + '\n')
#     fielnum = 0
#     list = os.listdir(dir)  #列出目录下的所有文件和目录
#     for line in list:
#         filepath = os.path.join(dir,line)
#         if os.path.isdir(filepath):  #如果filepath是目录，则再列出该目录下的所有文件
#             dirsize=getPathSize(dir+'/'+line)/1024/1024;
#             if (dirsize<2):
#                 myfile.write('   ' + line + '//'+bytes(dirsize)+'M'+ '\n')
#                 # shutil.copy(dir+'/'+line,  '/home/cc/temp/logs')
#                 for li in os.listdir(filepath):
#                     delfile=(filepath+ '/'+li)
#                     myfile.write(delfile+ '\n')
#                     #os.remove(delfile.decode('gb18030'))
#                     fielnum = fielnum + 1
#                     myfile.write('\n'+'all the file num is '+ str(fielnum)+ '\n')
#                 #os.rmdir(dir+'/'+line)
#                 #shutil.rmtree(dir+'/'+line)
#         # elif os.path:   #如果filepath是文件，直接列出文件名
#         #     shutil.copy(dir+'/'+line,  '/home/cc/temp/logs')
#         #     myfile.write('   '+line + '\n')
#         #     fielnum = fielnum + 1
#
# # dir = raw_input('please input the path:')
# def getPathSize(strPath):
#     if not os.path.exists(strPath):
#         return 0;
#
#     if os.path.isfile(strPath):
#         return os.path.getsize(strPath);
#
#     nTotalSize = 0;
#     for strRoot, lsDir, lsFiles in os.walk(strPath):
#         #get child directory size
#         for strDir in lsDir:
#             nTotalSize = nTotalSize + getPathSize(os.path.join(strRoot, strDir));
#
#             #for child file size
#         for strFile in lsFiles:
#             nTotalSize = nTotalSize + os.path.getsize(os.path.join(strRoot, strFile));
#
#     return nTotalSize;
#
# def moveFileto(sourceDir,  targetDir):
#     shutil.copy(sourceDir,  targetDir)
#
# def coverFiles(sourceDir,  targetDir):
#     for file in os.listdir(sourceDir):
#         sourceFile = os.path.join(sourceDir,  file)
#         targetFile = os.path.join(targetDir,  file)
#         #cover the files
#         if os.path.isfile(sourceFile):
#             open(targetFile, "wb").write(open(sourceFile, "rb").read())

def printAllFile(file_dir):
    fileList=[]
    hashLikst=[]
    dirList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 过滤系统文件
    filterList = ['.DS_Store']
    list=os.listdir(file_dir)
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
def createShardingDir(num):
    target=dir+num
    if (not os.path.exists(target)):
        print ("create "+target)
        os.mkdir(target)
    else:
        print (target+"has create")

def cutFile(file,num):
    src=dir+os.path.basename(file)
    print ("src:"+src)
    try:
        shutil.move(src,dir+num+"/")
    except OSError,errormsg:
        print'fi exist!',errormsg


# dir="/home/cc/share/tt/cc/y"
#dir='W://w'


dir='/Users/chen.cc/Downloads/tmp/ll/'
countFile = CountFile(dir)
start = countFile.run()
printAllFile(dir.decode('utf-8'))
countFile = CountFile(dir)
end = countFile.run()
print ("split file start:"+str(start)+"   end:"+str(end))



#old
#dir='F://迅雷下载'.decode('utf-8')
#myfile = open('list.txt','w')
#listdir(dir,myfile)
#myfile.close()

