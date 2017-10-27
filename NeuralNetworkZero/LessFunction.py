# -*- coding: utf8 -*-
#time:2017/10/25 下午1:09
#VERSION:1.0
#__OUTHOR__:guangguang
import numpy as np
#损失函数
class LessFunctions():
	def __init__(self,Yhat,Y):
		self.Yhat=Yhat
		self.Y=Y
	def LessTwo(self):
		L=(self.Yhat-self.Y)**2
		return L
	def VectorizationLessTwo(self):
		L=np.dot((self.Y-self.Yhat),(self.Y-self.Yhat).T)
		return L


#debug
if __name__ == "__main__":
    pass