from pprint import pprint

from framework.request import Request
from framework.response import Response
from framework.views import View


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        # pprint(environ)
        # print(request.__dict__)
        request = Request(environ)
        # print(f'request.headers: {request.headers}')
        # print(f'request.body.read(): {request.body.read()}')
        print(f'request.path: {request.path}')
        # print(f'request.query_params: {request.query_params}')
        view = self._get_view(request)
        # print(view)
        print(self._get_response(request, view))

        start_response('200 OK', [('Content-Type', 'text/html')])
        response = Response(request)
        return [response.response.encode()]

    def _get_view(self, request: Request):
        path = request.path
        # print(path)
        # print(f'*****{self.urls}')
        for url in self.urls:
            # print(f'*****{url}')
            if url.url == path:
                return url.view
        return None

    def _get_response(self, request: Request, view: View):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        else:
            return 'Упс'
