from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import User


class VerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    token = models.CharField(max_length = 100, unique = True)
    created_date = models.DateTimeField(_("Date Created") , auto_now_add = True)

    def __str__(self):
        return f"{self.user.username}-token"