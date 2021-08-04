import pyperclip
from user_account import User,Credentials

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
	create a new credential
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
    print("*"*40)
    print('\nWelcome to Password Locker')
    while True:
        print('Pick One: \n 1. Create Account \n 2. Login \n 3. Exit')
        user_pick = input().strip()


        if user_pick == '1': # Create Account
            print("*"*40 )
            print('To create a new Account')
            first_name = input('\nEnter your first name: ').strip
            last_name = input('\nEnter your last name: ').strip
            password = input('\nEnter your password: \n').strip

            save_user(create_user(first_name,last_name,password))
            print(f"New Account Created for : {first_name} {last_name}")

        elif user_pick == '2': # Login
            print("*"*40 )
            print('To Log In Enter Details: ')
            user_name = input('Enter your first name: \n').strip
            password = str(input('Enter your password: \n'))
            user_exists = verify_user(user_name,password)
            if user_exists == user_name:
                print(f'Welcome{first_name}. Please pick an option to continue\n')
                while True:
                    print('1. Create Credential \n2. Display Credentials \n3.Copy Password \n4. Exit' )
                    user_pick = input('Enter pick: ').strip()

                    if user_pick == '1': # Create credentials
                        print("Enter Credentials Details: ")
                        site_name = input("Enter site's name: ").strip
                        account_name = input("Enter Account's name: ").strip
                        while True:
                            print('Please choose an option for entering a password: \n 1. Enter existing password \n2. Generate password \n3. Exit')
                            password_choice = input("Enter your pick: \n").strip

                            if password_choice == '1':
                                password = input('Enter your passord: ').strip
                                break
                            elif password_choice == '2':
                                password = generate_password()
                                break
                            elif password_choice == '3':
                                break
                            else:
                                print('Wrong option. Please try another')
                        save_credential(create_credential(user_name,site_name,account_name,password))
                        print(f'/n Credential saved: Site Name: {site_name}, Account Name: {account_name}, Password: {password}')
                    
                    elif user_pick == '2': # Display credentials
                        if display_credentials(user_name):
                            print('Here are your credentials')
                            for credential in display_credentials(user_name):
                                print(f'Site Name: {site_name}, AccountName {account_name}, Password{password}')

                        else:
                            print('You have no credentials yet')

                    elif user_pick == '3': # Copy credentials
                        site_picked = input('Enter name name of credential to copy: ')
                        copy_credential(site_picked)



                    elif user_pick == '4':
                        print(f'Goodbye {first_name}')

                    else:
                        print('Wrong details entered')














        elif user_pick == '3': # Exit
            break

        else:
            print('Wrong input entered')










if __name__ == '__main__':
	main()