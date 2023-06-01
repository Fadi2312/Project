from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Etud

class EtudBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            etud = Etud.objects.get(username=username)
            if check_password(password, etud.password):
                return etud
        except Etud.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Etud.objects.get(pk=user_id)
        except Etud.DoesNotExist:
            return None
