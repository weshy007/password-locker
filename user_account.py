import string
import random
import pyperclip

global users_list

class User:
    '''
    Class to create user account and save their info
    '''
    # the global list of users
    users_list = []

    def __init__(self, first_name, last_name,password):
        '''
        Method for instance
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        Saving created users
        '''
        User.users_list.append(self)

class Credentials:
    '''
    Class to create account credentials, gen passwd and save info
    '''
    credentials_list = []
    user_credentials_list = []

    @classmethod
    def check_user(cls,first_name,password):
        '''
        checks details entered accross the users_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self, user_name,site_name,account_name,password):
        '''
        define properties and instance
        '''

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        saving newly created user instance
        '''
        #global list
        Credentials.credentials_list.append(self)

    def generate_password(size=8, char=string.ascii_lowercase+string.digits):
        '''
        Generating 8 char password
        '''
        gen_pass = ''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def display_credentials(cls,user_name):
        '''
        method to display the list of credentials saved
        '''
        user_credential_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credential_list.append(credential)

        return user_credential_list

    @classmethod 
    def find_by_site_name(cls, site_name):
        '''
        takes in the site_name returns credential that matches
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def copy_credential(cls, site_name):
        '''
        method that copies a credential's info after the credentials site  name is entered
        '''
        find_credential = Credentials.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)