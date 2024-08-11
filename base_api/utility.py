import logging
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import APIException


logger = logging.getLogger(__name__)

class CustomLoggingMixin:
    def log_request(self, request):
        logger.info(f"Request method: {request.method}, path: {request.path}, user: {request.user}")

class CustomerPagination(PageNumberPagination):
    page_size = 10


class CustomNotFoundException(APIException):
    status_code = 404
    default_detail = 'Object not found.'
    default_code = 'object_not_found'