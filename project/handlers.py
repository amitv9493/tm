from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    if isinstance(exc, ValidationError):
        return Response(
            data={"detail": str(exc)},
            status=400,
        )

    # Use the default exception handler for other exceptions
    return exception_handler(exc, context)
