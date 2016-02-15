from django.conf import settings
import shortuuid


class ImpressionMiddleware(object):

    def process_request(self, request):
        publisher_key = request.META.get('HTTP_PUBLISHER_KEY', None)
        if publisher_key:
            from apps.companies.models import Company
            try:
                publisher = Company.objects.get(publisher_key=publisher_key)
                request.publisher = publisher
            except Company.DoesNotExist:
                request.publisher = None
            request.visitor = request.get_signed_cookie('visitor', shortuuid.uuid())

    def process_response(self, request, response):
        publisher = getattr(request, 'publisher', None)
        if publisher:
            if request.visitor:
                visitor = request.visitor
            else:
                visitor = shortuuid.uuid()
            response.set_signed_cookie('visitor', visitor)
        return response
