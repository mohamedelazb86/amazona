from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class Login_Username_Email(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user=User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user=User.objects.get(username=username)
            except User.DoesNotExist:
                return None
            
        if user.check_password(password):
            return user
        return None