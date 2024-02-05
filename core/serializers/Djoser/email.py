from django.contrib.auth.tokens import default_token_generator
from djoser import email , utils
from djoser.conf import settings

from core.models import VerificationCode


class ActivationEmail(email.ActivationEmail):
    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()
        user = context.get("user")

        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)

        verification_code , created = VerificationCode.objects.get_or_create(user = user)
        verification_code.token = context['token']
        verification_code.save()
        return context


class ConfirmationEmail(email.ConfirmationEmail):
    def get_context_data( self ):
        # ActivationEmail can be deleted
        context = super().get_context_data()
        user = context.get("user")

        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)

        verification_code , created = VerificationCode.objects.get_or_create(user = user)
        verification_code.token = self.context['token']
        verification_code.save()
        return context

class PasswordResetEmail(email.PasswordResetEmail):
    def get_context_data( self ):
        # ActivationEmail can be deleted
        context = super().get_context_data()
        user = context.get("user")

        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)

        verification_code , created = VerificationCode.objects.get_or_create(user = user)
        verification_code.token = self.context['token']
        verification_code.save()
        return context

class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    def get_context_data( self ):
        # ActivationEmail can be deleted
        context = super().get_context_data()
        user = context.get("user")

        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)

        verification_code , created = VerificationCode.objects.get_or_create(user = user)
        verification_code.token = self.context['token']
        verification_code.save()
        return context