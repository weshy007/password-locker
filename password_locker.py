from user_account import User, Credentials

def create_user(fname,lname,password):
	'''
	create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	save a new user account
	'''
	User.save_user(user)

def verify_user(first_name,password):
	'''
    validation of the user before creating credentials	
    '''
	checking_user = Credentials.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	generate a password automatically
	'''
	gen_pass = Credentials.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	to create a new credential
	'''
	new_credential=Credentials(user_name,site_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	save a newly created credential
	'''
	Credentials.save_credentials(credential)

def display_credentials(user_name):
	'''
	display credentials saved by a user
	'''
	return Credentials.display_credentials(user_name)
	
def copy_credential(site_name):
	'''
	copy a credentials details to the clipboard
	'''
	return Credentials.copy_credential(site_name)

def main():
	print(' ')
	print('WELCOME TO PASSWORD LOCKER.')
	while True:
		print("*"*60)
		print('Use these codes to navigate: \n 1.Create an Account \n 2.Log In \n 3.Exit')
		user_pick = input('Enter Option: ').strip()
		if user_pick == '3':
			break

		elif user_pick == '1':
			print("*"*60)
			print('To create a new account: ')
			first_name = input('Enter your first name: ').strip()
			last_name = input('Enter your last name: ').strip()
			password = input('Enter your password: ').strip()
			save_user(create_user(first_name,last_name,password))

			print(f'New Account Created for: {first_name} {last_name} using Password: {password}')
		elif user_pick == '2':
			print("*"*60)
			print('To login, enter your account details \n')
			user_name = input('Enter your first name: ').strip()
			password = str(input('Enter your password:  '))
			user_exists = verify_user(user_name,password)

			if user_exists == user_name:
				print(f'\nWelcome {user_name.capitalize()}. Please choose an option to continue.')
				while True:
					print("*"*60)
					print('\n 1.Create a Credential \n 2.Display Credentials \n 3.Copy Password \n 4.Exit')
					short_code = input('Enter an Option: ').strip()
					print("*"*60)
					if short_code == '4':
						print(f'Goodbye {user_name.capitalize()}')
						break

					elif short_code == '1':
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print('\nPlease choose an option for entering a password: \n 1.Enter existing password \n 2.Generate a password \n 3.Exit')
							psw_choice = input('Enter an option: ').lower().strip()
							if psw_choice == '1':
								password = input('\nEnter your password: ').strip()
								break
							elif psw_choice == '2':
								password = generate_password()
								break
							elif psw_choice == '3':
								break
							else:
								print('Wrong option entered.Please try again.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}\n')

					elif short_code == '2':
						if display_credentials(user_name):
							print('Here is a list of all your credentials\n')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}\n')
						else:
							print("You don't seem to have any credentials saved yet\n")

					elif short_code == '3':
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)

					else:
						print('Wrong option entered.Please try again.')

			else: 
				print('Wrong Details. Try again or Create an Account.')		
		
		else:
			print("*"*60)
			print('Wrong option entered.Please try again.')

if __name__ == '__main__':
	main()