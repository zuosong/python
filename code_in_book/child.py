#-*-coding:UTF-8 -*-

class Parent:	#���常��
	parentAttr = 100
	def __ini__(self):
		print "���ø��๹�캯��"
	
	def parentMethod(self):
		print "���ø��෽��"
	
	def setAttr(self,attr):
		Parent.parentAttr = attr
	
	def getAttr(self):
		print "�������ԣ�",Parent.parentAttr

class Child(Parent):#��������
	def __ini__(self):
		print "�������๹�췽��"
	
	def childMethod(self):
		print '�������෽��child method'

c = Child()#ʵ��������
c.childMethod()#�������෽��
c.parentMethod()#���ø��෽��
c.setAttr(200)	#�ٴε��ø���ķ���
c.getAttr()	#�ٴε��ø���ķ���

