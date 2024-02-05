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

    phone_number = models.PositiveSmallIntegerField(
        _("Phone Number") ,
        default = 0,
        help_text = _("User's phone number") ,
        db_comment = _("User's phone number") ,
    )
    GENDER_CHOICES = [
        ('Male' , _('Male')) ,
        ('Female' , _('Female')) ,
        ('Prefer not to say' , _('Not_Preferred')) ,

    ]
    gender = models.CharField(
        _("Gender") ,
        max_length = 17 ,
        choices = GENDER_CHOICES ,
        help_text = _("User's gender") ,
        db_comment = _("User's gender") ,
        blank = True,
    )
    country = models.CharField(
        _("Country") ,
        max_length = 40 ,
        help_text = _("User's country") ,
        db_comment = _("User's country") ,
        blank = True,
    )

