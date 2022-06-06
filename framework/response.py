from jinja2 import Template
from framework.request import Request


class Response:
    def __init__(self, request: Request):
        self.response = self._get_response(request)

    def _get_response(self, request):
        path = request.path
        with open(f'framework/templates{path}.html', encoding='utf-8') as html:
            template = Template(html.read())
        return template.render()
