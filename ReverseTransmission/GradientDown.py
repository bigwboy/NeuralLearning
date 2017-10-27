# -*- coding: utf8 -*-
#time:2017/10/27 10:24
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
from  NeuralNetworkZero import ActivationFunction

class ActivationFunctionDrivative(ActivationFunction.ActivationFunction):
	def __init__(self):
		pass
	def SigmodDrivative(self):
		s=self.Sigmod()
		ds=s(1-s)
		return ds



#DEBUG
if __name__ == "__main__":
	pass