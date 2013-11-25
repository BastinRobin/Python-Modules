'''
	Author: Bastin Robins.J
	Desc: Simple Account
'''

class Account(object):
	def __init__(self):
		self.history = []
		self.storage = {}

	def create_account(self, name, accno):
		self.storage[accno] = name
		if(self.storage[accno]):	
			self.history.append("Account Created Successfully")
			print "Account Created Successfully"
		else:
			self.history.append("Check for errors")
			print "Check for errors"

	def del_account(self, accno):
		del self.storage[accno]
		if(self.storage[accno]):
			print "Not Removed user!!"
		else:
			print "Removed user Successfully"

	def edit_account(self, name, accno):
		self.storage[accno] = name
		print "Changes made Successfully"

	def view_users(self):
		for key, value in storage:
			print key, value


if __name__ == '__main__':
	
	data = Account()
	while True:
		print '1. Add'
		print '2. Delete'
		print '3. Edit'
		print '4. View'
		print '5. Exit'
		n = input()
		if n == 1:
			print 'Enter Name and Acc No:'
			name = raw_input()
			acc = raw_input()
			data.create_account(name, acc)
		elif n == 2:
			print "Enter Acc No:"
			acc = raw_input()
			data.del_account(acc)
		elif n == 3:
			print "Enter Name or Acc No:"
			name = raw_input()
			acc = raw_input()
			data.edit_account(name,accno)
		elif n == 4:
			data.view_users
