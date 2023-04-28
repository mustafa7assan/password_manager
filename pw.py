import sys
import pyperclip

passwords = {}


def load_passwords():
    password_file = open('passwords.txt')
    lines = password_file.readlines()
    for line in lines:
        account, password = line.strip().split(',')
        passwords[account] = password
    password_file.close()


def add_password(account, password):
    password_file = open('passwords.txt', 'a')
    password_file.write(f'{account},{password}')
    password_file.close()


load_passwords()


def add_account():
    account = input('Account name: ')
    password = input('Account password : ')
    passwords[account] = password
    add_password(account, password)
    print('New account is added.')


if len(sys.argv) < 2:
    print('Usage: python3 pw.py [account] - copy account password ')
    sys.exit()


account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'{account} password is copied to clipboard')
else:
    print(f'There no account named {account}')
    add = input('Do want to add to it password manager [Y/N]: ')
    if add.lower() == 'y' or add.lower() == 'yes':
        add_account()
