from rest_framework import serializers
from dj_rest_auth.serializers import PasswordResetSerializer
from apps.users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'profile_picture']

# Custom URL Generator
def custom_url_generator(request, user, temp_key):
    domain_override = 'localhost:5173'  # Force the frontend domain
    uid = user.pk
    return f"http://{domain_override}/reset-password/{uid}/{temp_key}/"

# Custom Password Reset Serializer
class CustomPasswordResetSerializer(PasswordResetSerializer):
    def save(self):
        # Force the domain and URL generator
        opts = {
            'url_generator': custom_url_generator,  # Use the custom URL generator
            'use_https': False,  # Ensure HTTP or HTTPS is set explicitly
            'email_template_name': 'registration/password_reset_email.html',  # Custom email template
            'extra_email_context': {
                'site_name': 'Your Site Name',  # Optional: Set your site name
            },
        }
        super().save(**opts)
