from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    """
    API view for the root route.
    This view returns a welcome message for the backend of Little Angels' Site.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: JSON response containing the welcome message.
    """
    return Response({
        "message": "Welcome to the Backend of Little Angels' Site"
    })


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    """
    Custom API view for logging out a user.
    This view clears the JWT authentication and refresh cookies to log out the user.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: Empty response with cleared JWT cookies.
    """
    response = Response()
    # Clear JWT authentication cookie
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    # Clear JWT refresh cookie
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
