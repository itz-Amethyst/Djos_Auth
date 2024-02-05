from datetime import datetime

from django.utils import timezone
from djoser import utils
from djoser.serializers import UidAndTokenSerializer as BaseActivationSerializer , PasswordSerializer , \
    PasswordRetypeSerializer , UsernameRetypeSerializer , UsernameSerializer
from rest_framework.exceptions import ValidationError

from core.models import VerificationCode , User


class UIUDTokenSerializer(BaseActivationSerializer):

    def validate( self , attrs ):
        # validated_data = super().validate(attrs)

        try:
            uid = utils.decode_uid(self.initial_data.get("uid" , ""))
            self.user = User.objects.get(pk = uid)
        except (User.DoesNotExist , ValueError , TypeError , OverflowError):
            key_error = "invalid_uid"
            raise ValidationError(
                {"uid": [self.error_messages[key_error]]} , code = key_error
            )

        is_token_valid = self.context["view"].token_generator.check_token(
            self.user , self.initial_data.get("token" , "")
        )


        if is_token_valid:
            # Check if the token has expired (created more than 5 minutes ago)
            token_created_time = self.user.verificationcode.created_date
            current_time_naive = timezone.make_naive(timezone.now)

            token_created_time_naive = timezone.make_naive(token_created_time)

            # Now both datetimes are offset-naive, and you can calculate the time difference
            time_difference = current_time_naive - token_created_time_naive

            if time_difference.total_seconds() > 300:  # 5 minutes = 300 seconds
                raise ValidationError({"token": ["Token has expired"]} , code = "expired_token")

            return validated_data
        else:
            key_error = "invalid_token"
            raise ValidationError(
                {"token": [self.error_messages[key_error]]} , code = key_error
            )


class ActivationSerializer(UIUDTokenSerializer):
    pass

class PasswordResetConfirmSerializer(UIUDTokenSerializer, PasswordSerializer):
    pass

class PasswordResetConfirmRetypeSerializer(UIUDTokenSerializer, PasswordRetypeSerializer):
    pass

class UsernameResetConfirmSerializer(UIUDTokenSerializer, UsernameSerializer):
    pass

class UsernameResetConfirmRetypeSerializer(UIUDTokenSerializer, UsernameRetypeSerializer):
    pass