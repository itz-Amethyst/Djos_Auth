from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name = _("Email") ,
        help_text = _("this is a email for user") ,
        db_comment = _("this is a email for a user") ,
        unique = True ,
    )