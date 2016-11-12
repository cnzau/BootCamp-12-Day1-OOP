import unittest

from app import logic

class PrepaidCard_TestCase(unittest.TestCase):
	def setUp(self):
		self.logic = PrepaidCard()

	def tearDown(self):
		del self.logic

	def test_prepaid_card_is_instance_of_prepaid_banking(self):
		self.assertTrue(isinstance(self.logic, PrepaidBanking), msg='PrepaidCard is not a subclass of PrepaidBanking')

	def test_prepaid_card_can_deposit_valid_amounts(self):
		balance = self.logic.deposit(100)
		self.assertEquals(balance, 100)

	def test_prepaid_card_cannot_spend_more_than_current_balance(self):
		message = self.logic.withdraw(100)
		self.assertEquals(message, 'Cannot spend beond the current account balance', msg="You can't go beynd the card minimum balance")

	def test_prepaid_card_can_spend_valid_cash_amounts(self):
		self.logic.deposit(600)
		self.logic.online_payment(500)
		self.assertEquals(self.logic.balance, 100, msg='Incorrect balance after withdrawal')


class PremiumPrepaidCardTestCases(unittest.TestCase):
	def setUp(self):
		self.prem = PremiumPrepaidCard()

	def tearDown(self):
		del self.prem

	def test_premium_prepaid_card_is_instance_of_prepaid_banking(self):
		self.assertTrue(isinstance(self.logic, PrepaidBanking), msg='PrepaidCard is not a subclass of PrepaidBanking')

	def test_premium_prepaid_card_can_deposit_valid_amounts(self):
		balance = self.logic.deposit(100)
		self.assertEquals(balance, 100)

	def test_premium_prepaid_card_cannot_spend_more_than_current_balance(self):
		message = self.logic.withdraw(100)
		self.assertEquals(message, 'Cannot spend beond the current account balance', msg="You can't go beynd the card minimum balance")

	def test_prepaid_card_can_spend_valid_cash_amounts(self):
		self.logic.deposit(600)
		self.logic.online_payment(500)
		self.assertEquals(self.logic.balance, 100, msg='Incorrect balance after withdrawal')


if __name__ == "__main__":
	unittest.main()
