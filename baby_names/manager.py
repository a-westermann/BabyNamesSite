from .models import Account, AccountData
from django.http import HttpResponse, HttpRequest


def get_account_data(email):
    login_query = Account.objects.raw(f"SELECT * FROM baby_names_account WHERE email = '{email}'")
    account = None
    if login_query:
        print(f'Found account: {login_query[0].email}')
        account = login_query[0]
    else:
        # Make account for now. Need to do a sign up verify step for real though
        account = Account()
        account.email = email
        account.save()
        print(f'new account set up for {account.email}')
    return account

def get_name(session):
    # Connect to postgresql
    return ''


