import unittest

from logic import PrepaidBanking

class PrepaidCard_TestCase(unittest.TestCase):
	def test_prepaid_deposit(self):
		self.assertEqual(PrepaidBanking.deposit(50), (50 + amount))

	def test_prepaid_deposit(self):
		self.assertEqual(PrepaidBanking.deposit(0), msg="Your card has not been recharged")

	def tes_prepaid_deposit(self):
		self.assertEqual(PrepaidBanking.deposit(-4), msg="Invalid transaction attempt!")

	def test_prepaid_online_payment(self):
		self.assertEqual(PrepaidBanking.online_payment(10), msg="You can't go beyond the card minimum balance")

	def test_prepaid_online_payment(self):
		self.assertEqual(PrepaidBanking.online_payment(0), msg="No charges were incurred")

	def test_prepaid_online_payment(self):
		self.assertEqual(PrepaidBanking.online_payment(9), 9.9)

	def test_prepaid_online_payment(self):
		self.assertEqual(PrepaidBanking.online_payment(50), 57.7)

	def test_prepaid_online_payment(self):
		self.assertEqual(PrepaidBanking.online_payment(250), 300)

	def test_premium_prepaid_deposit(self):
		self.assertEqual(PrepaidBanking.deposit(50), 100)

	def test_premium_prepaid_deposit(self):
		self.assertEqual(PrepaidBanking.deposit(45), msg="Insufficient deposit amount")

	def test_premium_prepaid_deposit(self):
		self.assertEqual(PrepaidBanking.online_payment(50), msg="You can't go beyond the card minimum balance")

	def test_premium_prepaid_deposit(self):
		self.assertEqual(PrepaidBanking.online_payment(0), msg="No charges were incurred")

	def test_premium_prepaid_deposit(self):
		self.assertEqual(PrepaidBanking.deposit(900), 990)

if __name__ == "__main__":
	unittest.main()
