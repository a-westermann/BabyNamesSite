from django.shortcuts import render
from django.http import HttpResponse
from baby_names import manager  # need to specify this for directory reasons
from baby_names.models import Account


# each HttpRequest arg contains a session attribute (a dict)
# you can read and write to request.session
def index(request):
    # have a form for logging in, then cache the account

    # user_account = Account()

    # user_account.visible_email
    # request.session['user_account'] = user_account

    return render(request, 'baby_names/index.html',
                  {
                      # 'email': user_account.email
                  })


def view_new_name(request):
    new_name = manager.get_name()
    return HttpResponse()
