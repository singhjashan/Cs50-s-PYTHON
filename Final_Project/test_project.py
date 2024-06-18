#


import unittest
from project import Bank

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank(123456, "Jashanpreet Singh", 1000.0)

    def test_open(self):
        result = self.bank.open(123456, "Jashanpreet Singh", 1000.0)
        self.assertEqual(result, {"Account number": 123456, "Customer name": "Jashanpreet Singh", "Balance": 1000.0})

    def test_deposit(self):
        result = self.bank.deposit(500)
        self.assertEqual(result, {"Account number": 123456, "Customer name": "Jashanpreet Singh", "Balance": 1500.0})

    def test_withdraw(self):
        result = self.bank.withdraw(200)
        self.assertEqual(result, {"Account number": 123456, "Customer name": "Jashanpreet Singh", "Balance": 800.0})

if __name__ == '__main__':
    unittest.main()
