class Request:

    def __init__(self, environ: dict):
        self.headers = self._get_http_headers(environ)
        self.method = environ['REQUEST_METHOD'].lower()
        self.body = environ.get('wsgi.input')
        self.query_params = self._get_query_params(environ)
        self.path = environ['PATH_INFO']

    def _get_http_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                headers[key[5:]] = value
        return headers

    def _get_query_params(self, environ):
        data = environ['QUERY_STRING'].split('&')
        params = {}
        for param in data:
            if param:
                key, value = param.split('=')
                if params.get(key):
                    params[key].append(value)
                else:
                    params[key] = [value]
        return params
