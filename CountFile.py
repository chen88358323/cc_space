# -*- coding: utf-8 -*-
import os


class CountFile:

    def __init__(self,dir):
        self.root = dir
        self.Num = 0

    def countfile(self, path):
        if not os.path.isdir(path):
            return
        fileList = os.listdir(path)
        for fileName in fileList:
            fileName = os.path.join(path, fileName)
            if os.path.isdir(fileName):
                self.countfile(fileName)
            else:
                self.Num += 1

    def run(self):
        self.countfile(self.root)


if __name__ == "__main__":
    A = CountFile()
    A.run()