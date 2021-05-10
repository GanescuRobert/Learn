
class CharityFund:
	def __init__(self,balance=1000000):
		self.balance = balance
	def save_fund(self,amount):
		self.balance += amount
	def spend_fund(self,amount):
		self.balance -= amount
	def invest(self, return_rate):
		self.balance *= 1 + return_rate
	def get_balance(self):
		if self.balance < 0:
			print( "You got a deficit of " + str(-self.balance))
		return self.balance
	def is_danger(self):
		if self.balance < 50000:
			print('Danger. You have '+str(self.balance)+' left')
		return self.balance < 50000

help_elderly = CharityFund ()
help_elderly.spend_fund(200000)
print(help_elderly.get_balance())

help_elderly.invest(-0.05)
print(help_elderly.get_balance())

help_elderly.save_fund(100000)
print(help_elderly.get_balance())

help_elderly.spend_fund(900000)
print(help_elderly.get_balance())

print(help_elderly.is_danger())
