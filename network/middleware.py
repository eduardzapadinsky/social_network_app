from django.utils import timezone

from .models import UserRequest


class RequestTrackingMiddleware:
    """
    Middleware for tracking user requests and updating the UserRequest model.
    This middleware is responsible for logging user requests and updating the UserRequest model
    with the timestamp of the latest request.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Only log the request if the user is authenticated
        if request.user.is_authenticated:
            user = request.user

            # Retrieve or create the UserRequestLog model for the user
            user_request_log, created = UserRequest.objects.get_or_create(user=user)

            # Update the timestamp for the latest request
            user_request_log.timestamp = timezone.now()
            user_request_log.save()

        return response
