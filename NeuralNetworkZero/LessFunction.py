# -*- coding: utf8 -*-
#time:2017/10/25 下午1:09
#VERSION:1.0
#__OUTHOR__:guangguang

#损失函数
class LessFunctions():
	def __init__(self,Yhat,Y):
		self.Yhat=Yhat
		self.Y=Y
	def Less(self):
		L=(self.Yhat-self.Y)**2
		return L




#debug
if __name__ == "__main__":
    pass