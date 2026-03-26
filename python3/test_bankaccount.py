import unittest
from tests import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1)
        self.account.deposit(100)
    def test_withdraw(self):
        # Arrange
        a = 50
        # Act
        result = self.account.withdraw(a)
        # Assert
        self.assertTrue(result)
    def tearDown(self):
        pass

#----------------------------------------------------------------------------------------
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass