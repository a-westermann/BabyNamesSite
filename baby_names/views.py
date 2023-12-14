from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from baby_names import manager
from baby_names.models import Account


# each HttpRequest arg contains a session attribute (a dict)
# you can read and write to request.session
def index(request):
    # user_account = Account()

    # user_account.visible_email
    # request.session['user_account'] = user_account

    return render(request, 'baby_names/index.html')

@csrf_exempt
def account_landing(request):
    print(f"requested log in for {request.POST['email']}")
    # have a form for logging in, then cache the account
    # this sets up a new account if one doesn't exist
    account = manager.get_account_data(request.POST['email'])
    request.session['email'] = account.email
    return render(request, 'baby_names/account_landing.html',
                  {'email': account.email})


def view_new_name(request):
    new_name = manager.get_name(request.session)
    return render(request, 'baby_names/view_new_name.html')
