# middleware.py

import logging
import json
from datetime import datetime

logger = logging.getLogger(__name__)

class LogNon200ResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capture the request headers and body.
        request_headers = dict(request.headers)
        # request_body = None
        response = self.get_response(request)
        status_code = response.status_code
        if status_code != 200:
            # Capture the error response content.
            response_content = response.content.decode('utf-8')

            # Get the current timestamp.
            timestamp = datetime.now().isoformat()

            logger.error(
                '\n'
                f"Timestamp: {timestamp}\n"
                f"Non-200 response: {status_code} {request.method} {request.path} by user {request.user}\n"
                f"Request Headers: {request_headers}\n"
                # f"Request Body: {request_body}\n"
                f"Error Response: {response_content}"
                '\n'
            )

        return response
