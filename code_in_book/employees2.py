#-*-coding:UTF-8 -*-

class Employee:
	'����Ա���Ļ���'
	empCount = 0
	
	def __ini__(self,name,salary):
		self.name = name
		self.salary =salary
		Employee.empCount += 1
	
	def displayCount(self):
		print "Total Employee %d" %Employee.empCount
	
	def displayEmploy(self):
		print "Name: " ,self.name,",Salary: ",self.salary

print "Employee.__doc__:",Employee.__doc__
print "Employee.__name__:",Employee.__name__
print "Employee.__module__:",Employee.__module__
print "Employee.__bases__:",Employee.__bases__
print "Employee.__dict__:",Employee.__dict__