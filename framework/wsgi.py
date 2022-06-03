from pprint import pprint

from request import Request


def app(environ, start_response):
    pprint(environ)
    request = Request(environ)
    print(f'request.headers: {request.headers}')
    print(f'request.body.read(): {request.body.read()}')
    print(f'request.path: {request.path}')
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Wake up, Neo']
