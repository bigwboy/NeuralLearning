# -*- coding: utf8 -*-
#time:2017/10/20 10:39
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
import math,numpy

#激励函数
class ActivationFunction():
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
	def LeakageRelu(self):
		a=numpy.where(self.Z>0,self.Z,(0.01*self.Z))
		return a

ActivationFunctionType=["Sigmod","Tanh","Relu","LeakageRelu"]

#DEBUG
if __name__ == "__main__":
	pass