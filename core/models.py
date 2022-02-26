from django.db import models
from allauth.account.signals import user_logged_in
from django.contrib.auth import get_user_model

User = get_user_model()

#creating reciever
def user_logged_in_reciever(request, user, **kwargs):
    print(request)
    print(user)

user_logged_in.connect(user_logged_in_reciever,sender=User)