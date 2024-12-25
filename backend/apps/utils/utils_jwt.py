import jwt
from datetime import datetime, timedelta
from django.conf import settings


def generate_jwt(user, expires_in=60*60):  # Expiră într-o oră
    payload = {
        'user_id': user.id,
        'username': user.username,
        'role': user.userprofile.role,  # Folosește profilul pentru a obține rolul
        'exp': datetime.utcnow() + timedelta(seconds=expires_in),
        'iat': datetime.utcnow(),
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token has expired'}
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token'}

