from django.db import models


class Account(models.Model):
    # def __init__(self, email):
    #     super(Account, self).__init__()
        # self.email = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    linked_email = models.CharField(max_length=40)  # contains email of account of 'spouse'
        #TODO: hook directly to postgresql using this info to find rated names
    # visible_email = ''

class AccountData(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

