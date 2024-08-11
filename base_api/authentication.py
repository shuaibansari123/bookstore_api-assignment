from django.contrib.auth.backends import BaseBackend
from .models import Customer, Author
from django.db.models import Q

class CustomerAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            print('customer.. ' , email , password , kwargs)
            user = Customer.objects.get(Q(email=email) | Q(username=email))
            print('cus= ' , user)
            if user.check_password(password):
                print('matche cus')
                return user
            print('wrong pass')
        except Customer.DoesNotExist:
            print('custom does not match ')
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None

class AuthorAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            print('auther..')
            user = Author.objects.get(Q(email=username) | Q(username=username))
            if user.check_password(password):
                print('correct pass')
                return user
            print('wrong pass')
        except Author.DoesNotExist:
            print('auth does not exists')
            return None

    def get_user(self, user_id):
        try:
            print('get user ...')
            return Author.objects.get(pk=user_id)
        except Author.DoesNotExist:
            return None