from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name = _("Email") ,
        help_text = _("this is a email for user") ,
        db_comment = _("this is a email for a user") ,
        unique = True ,
    )

    phone_number = models.BigIntegerField(
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

    company_name = models.CharField(
        _("Company Name"),
        max_length = 70,
        help_text = _("Company's name"),
        db_comment = _("Company's name"),
        default = ''
    )


    def generate_token( self ):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
