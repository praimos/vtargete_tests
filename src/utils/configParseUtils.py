import configparser
import os


parser = configparser.ConfigParser()
parser.read(f'{os.path.dirname(os.path.abspath(__file__))}\\configs\\authconf.ini')

vk_login = parser.get('authvk', 'login')
vk_password = parser.get('authvk', 'password')

