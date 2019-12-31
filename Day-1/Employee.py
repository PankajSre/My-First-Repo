class Employee:
	__salary = 10
	def __init__(self,fname,lname,age):
		print('This is Constructor')
		self.fname = fname
		self.lname= lname
		self.age = age
		
	def full_name(self):
		return '{} {}'.format(self.fname,self.lname)
	def email_id(self):
		return '{}.{}@niit.com'.format(self.fname,self.lname)
employee = Employee('Pankaj','Saini',34)
print(employee.full_name())
print(employee.email_id())
print(employee.age)
employee.age = 25
print('Updated Age : ', employee.age)
print(Employee._Employee__salary)
