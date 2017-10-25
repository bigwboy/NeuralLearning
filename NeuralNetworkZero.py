# -*- coding: utf8 -*-
#time:2017/10/20 10:39
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
import math,numpy

#线性和
class LineSum():
	def __index__(self,W,X,B):
		self.W=W
		self.X=X
		self.B=B
	def Sum(self):
		Z=self.W*self.X+self.B
		return Z

#激励函数
class ActivationFunctions():
	def __init__(self,Z):
		self.Z=Z
	#sigmoid
	def Sigmod(self):
		a=1/(1+math.exp(-self.Z))
		return a
	#tanh
	def Tanh(self):
		a=(math.exp(self.Z)-math.exp(-self.Z))/(math.exp(self.Z)+math.exp(-self.Z))
		return a
	#Relu
	def Relu(self):
		a=numpy.where(self.Z>0,self.Z,0)
		return a
	#LeakageRelu
	def Leakage(self):
		a=numpy.where(self.Z>0,self.Z,(0.01*self.Z))
		return a

#损失函数
class LessFunctions():
	def __index__(self,Yhat,Y):
		self.Yhat=Yhat
		self.Y=Y
	def Less(self):
		L=(self.Yhat-self.Y)**2
		return L


#DEBUG
if __name__ == "__main__":
	pass