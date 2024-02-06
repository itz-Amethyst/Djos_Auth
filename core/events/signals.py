import phonenumbers
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from phonenumbers import geocoder
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from core.models import User


# Can remove the validation here
@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, **kwargs):
    if not instance.id:
        if instance.phone_number:
            with transaction.atomic():
                try:
                    parsed_number = phonenumbers.parse(instance.phone_number , None)
                    if not phonenumbers.is_valid_number(parsed_number):
                        raise ValidationError(_("Invalid phone number"))

                    # country_code = phonenumbers.region_code_for_number(parsed_number)

                    # Getting region information completed
                    country_code = geocoder.country_name_for_number(parsed_number , 'en')

                    # Getting region information State or city of country if needed
                    # Region = geocoder.description_for_number(phoneNumber , 'en')

                    if country_code is '' or None:
                        raise ValidationError(_("Unable to determine country from the phone number"))

                    instance.country = country_code
                except ValidationError as e:
                    raise ValidationError(e.detail)