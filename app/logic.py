class PrepaidBanking():
	"""
		Class for a Prepaid card Banking solution in US-Dollars
		There are two other classes that inherits from this main
		class.
	"""

	def deposit():
		pass

	def online_payment():
		pass

class PrepaidCard(PrepaidBanking):
	"""
		1. Currency in US-Dollars
		2. More flexible limits
		3. Which comes at a price of transaction charges
	"""

	def __init__(self, balance):
		self.balance = balance

	def deposit(self, amount):
		self.amount = amount
		if self.amount > 0:
			self.balance += amount
			return self.balance
		elif self.amount < 0:
			return "Invalid transaction attempt!"
		else:
			return "Your card has not been recharged"

	def online_payment(self, amoount):
		if amount > self.balance:
			return "Transuction has been rejected!"

		elif self.balance == 10:
			return "You can't go beyond the card minimum balance"

		elif amount == 0:
			return "No charges were incurred"

		else:
			if amount in range(1, 10):
				self.balance -= (amount + (amount * 0.1))
			elif amount in range(11, 100):
				self.amount -=  (amount + (amount * 0.15))
			elif amount > 100:
				self.balance -= (amount + (amount * 0.2))
		return self.balance

class PremiumPrepaidCard(PrepaidBanking):
	"""
		1. Currency in US-Dollars
		2. Premium cards have a higher limit
		3. But they enjoy transactions with no extra charges
	"""

	def __init__(self):
		self.balance = 100

	def deposit(self, amount):
		self.amount = amount
		if self.amount >= 50:
			return "Insufficient deposit amount"
		else:
			self.balance += amount
		return self.balance

	def online_payment(self, amount):
		self.amount = amount
		if amount > self.balance:
			return "Transuction has been rejected!"
		elif self.balance == 50:
			return "You can't go beyond the card minimum balance"
		elif amount == 0:
			return "No charges were incurred"
		else:
			self.balance -= (amount * 0.1)
		return self.balance
		