#-*-coding:UTF-8 -*-

class Parent:	#���常��
	parentAttr = 100
	def __ini__(self):
		print "���ø��๹�캯��"
	
	def myMethod(self):
		print "���ø��෽��"
	
	def setAttr(self,attr):
		Parent.parentAttr = attr
	
	def getAttr(self):
		print "�������ԣ�",Parent.parentAttr

class Child(Parent):#��������
	def __ini__(self):
		print "�������๹�췽��"
	
	def myMethod(self):
		print '�������෽��child method'

c = Child()#ʵ��������
c.myMethod()#�������෽��
c.setAttr(200)	#�ٴε��ø���ķ���
c.getAttr()	#�ٴε��ø���ķ���

