from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import User


class VerificationCode(models.Model):
    RESET_PASSWORD = 'reset_password'
    ACTIVATION = 'activation'
    RESET_USERNAME = 'reset_username'

    SECTION_CHOICES = [
        (RESET_PASSWORD , _('Reset Password')) ,
        (ACTIVATION , _('Activation')) ,
        (RESET_USERNAME , _('Reset Username')) ,
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    token = models.CharField(max_length = 100, unique = True)
    created_date = models.DateTimeField(_("Date Created") , auto_now_add = True)
    is_active = models.BooleanField(_("Is Active"), default = True)
    section = models.CharField(_("Section") , max_length = 20 , choices = SECTION_CHOICES, default = 'Not Defined')


    def __str__(self):
        return f"{self.user.username}-token"