#-*- coding:UTF-8 -*-

class JustCounter:
	__secretCount = 0 #˽�б���
	publicCount = 0 #��������
	
	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount#�ᱨ��ʵ�����ܷ���˽�б���
print counter._JustCounter__secretCount