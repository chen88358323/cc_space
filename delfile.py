#-*-encoding:utf-8-*-
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
import shutil
def listdir(dir,file):
    #print dir
    file.write(dir + '\n')
    fielnum = 0
    list = os.listdir(dir)  #列出目录下的所有文件和目录
    for line in list:
        filepath = os.path.join(dir,line)
        if os.path.isdir(filepath):  #如果filepath是目录，则再列出该目录下的所有文件
            dirsize=getPathSize(dir+'/'+line)/1024/1024;
            if (dirsize<2):
                myfile.write('   ' + line + '//'+bytes(dirsize)+'M'+ '\n')
                # shutil.copy(dir+'/'+line,  '/home/cc/temp/logs')
                for li in os.listdir(filepath):
                    delfile=(filepath+ '/'+li)
                    myfile.write(delfile+ '\n')
                    #os.remove(delfile.decode('gb18030'))
                    fielnum = fielnum + 1
                    myfile.write('\n'+'all the file num is '+ str(fielnum)+ '\n')
                #os.rmdir(dir+'/'+line)
                #shutil.rmtree(dir+'/'+line)
        # elif os.path:   #如果filepath是文件，直接列出文件名
        #     shutil.copy(dir+'/'+line,  '/home/cc/temp/logs')
        #     myfile.write('   '+line + '\n')
        #     fielnum = fielnum + 1

# dir = raw_input('please input the path:')
def getPathSize(strPath):
    if not os.path.exists(strPath):
        return 0;

    if os.path.isfile(strPath):
        return os.path.getsize(strPath);

    nTotalSize = 0;
    for strRoot, lsDir, lsFiles in os.walk(strPath):
        #get child directory size
        for strDir in lsDir:
            nTotalSize = nTotalSize + getPathSize(os.path.join(strRoot, strDir));

            #for child file size
        for strFile in lsFiles:
            nTotalSize = nTotalSize + os.path.getsize(os.path.join(strRoot, strFile));

    return nTotalSize;
def moveFileto(sourceDir,  targetDir):
    shutil.copy(sourceDir,  targetDir)
def coverFiles(sourceDir,  targetDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        #cover the files
        if os.path.isfile(sourceFile):
            open(targetFile, "wb").write(open(sourceFile, "rb").read())
# dir="/home/cc/share/tt/cc/y"
#dir='W://w'
dir='F://迅雷下载'.decode('utf-8')
myfile = open('list.txt','w')
listdir(dir,myfile)
myfile.close()
