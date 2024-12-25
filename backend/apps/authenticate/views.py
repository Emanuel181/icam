import json
import logging
from functools import wraps

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.middleware.csrf import get_token

from ..ideas.models import UserProfile
from ..utils.utils_jwt import generate_jwt, decode_jwt


def jwt_required(roles=None):
    # This returns a decorator
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return JsonResponse({'error': 'Authorization header is missing or invalid'}, status=401)

            token = auth_header.split(' ')[1]
            decoded = decode_jwt(token)

            if 'error' in decoded:
                return JsonResponse(decoded, status=401)

            # Check roles, if specified
            if roles and decoded.get('role') not in roles:
                return JsonResponse({'error': 'Access denied: insufficient permissions'}, status=403)

            # Attach user information to the request
            request.user_id = decoded['user_id']
            request.username = decoded['username']
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

# Protected view accessible by all authenticated users
@jwt_required()
def protected_view(request):
    return JsonResponse({
        'message': f'Hello, user {request.user_id} ({request.username})!'
    }, status=200)


@jwt_required(roles=['mentor'])
def mentor_view(request):
    return JsonResponse({'message': 'Welcome, mentor!'}, status=200)


@jwt_required(roles=['student'])
def student_view(request):
    return JsonResponse({'message': 'Welcome, student!'}, status=200)


def login_view(request):
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'error': 'Username and password are required'}, status=400)

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user:
                token = generate_jwt(user)
                return JsonResponse({'token': token}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

def register_view(request):
    try:
        if request.method == 'POST':
            import json

            # Check for empty body
            if not request.body:
                return JsonResponse({'error': 'Request body is empty'}, status=400)

            data = json.loads(request.body)

            # Extract fields from JSON data
            username = data.get('username')
            password = data.get('password')
            role = data.get('role')

            # Validate required fields
            if not username or not password or not role:
                return JsonResponse({'error': 'All fields (username, password, role) are required'}, status=400)

            # Check if the user already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            # Create the user
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(user=user, role=role)

            return JsonResponse({'message': 'User created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

def refresh_token_view(request):
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            token = data.get('token')
            if not token:
                return JsonResponse({'error': 'Token is required'}, status=400)

            decoded = decode_jwt(token)
            if 'error' in decoded:
                return JsonResponse(decoded, status=401)

            # Generate a new token
            user_id = decoded['user_id']
            user = User.objects.get(id=user_id)
            new_token = generate_jwt(user)
            return JsonResponse({'token': new_token}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
