from django.http import HttpResponseBadRequest


class ApiVersionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_version = request.META.get('HTTP_VERSION')
        print(api_version)
        if api_version not in ['v1', 'v2']:
            return HttpResponseBadRequest('Invalid API version')
        request.api_version = api_version
        response = self.get_response(request)
        return response
