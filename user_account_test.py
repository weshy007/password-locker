import unittest
import pyperclip
from user_account import User, Credentials

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviors.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Jo','Weshy','1234')

	def test__init__(self):
		'''
		Test to if check the initialization of user instances is properly done
		'''
		self.assertEqual(self.new_user.first_name,'Jo')
		self.assertEqual(self.new_user.last_name,'Weshy')
		self.assertEqual(self.new_user.password,'1234')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)