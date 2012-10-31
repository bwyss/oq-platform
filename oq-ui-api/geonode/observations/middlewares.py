from django import http

XS_SHARING_ALLOWED_ORIGINS = '*'
XS_SHARING_ALLOWED_METHODS = 'POST,GET,OPTIONS,PUT,DELETE'
XS_SHARING_ALLOWED_HEADERS = 'ORIGIN, X-REQUESTED-WITH, CONTENT-TYPE'


class XsSharing(object):
    """
        This middleware allows cross-domain XHR using the html5 postMessage API.

        eg.
        Access-Control-Allow-Origin: http://foo.example
        Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
        Access-Control-Allow-Methods: ["Content-Type"]

    """

    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = XS_SHARING_ALLOWED_METHODS
            response['Access-Control-Allow-Headers'] = XS_SHARING_ALLOWED_HEADERS
            return response

        return None

    def process_response(self, request, response):
        # Avoid unnecessary work
        if response.has_header('Access-Control-Allow-Origin'):
            return response

        response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = XS_SHARING_ALLOWED_METHODS
        response['Access-Control-Allow-Headers'] = XS_SHARING_ALLOWED_HEADERS

        return response