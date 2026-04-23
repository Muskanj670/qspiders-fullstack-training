from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend

class EmailorUserBackend(ModelBackend):
    def authenticate(self,request,username = None, password = None, **kwargs):
        try:
            user = User.objects.get(Q(username = username) | Q (email = username))
        except User.DoesNotExist:
            raise "Error"
        if user.check_password(password):
            return user
        return None
