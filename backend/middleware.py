# backend/middleware.py
from django.utils.deprecation import MiddlewareMixin

class CustomSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.session.session_key:
            request.session.create()

# Add this middleware to your MIDDLEWARE setting
