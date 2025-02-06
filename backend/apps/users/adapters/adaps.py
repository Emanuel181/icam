from allauth.account.adapter import DefaultAccountAdapter
from dj_rest_auth.serializers import PasswordResetSerializer

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        # Generate confirmation link pointing to Vue frontend
        return f"http://localhost:5173/email-confirmed?key={emailconfirmation.key}"
