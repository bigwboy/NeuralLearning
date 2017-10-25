# -*- coding: utf8 -*-
#time:2017/10/25 下午1:28
#VERSION:1.0
#__OUTHOR__:guangguang

from numpy import *

# load data 导入数据
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []; labelMat = []
    fd = open(fileName)
    for line in fd.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat




#debug
if __name__ == "__main__":
    pass