from framework.views import View


class HomePage(View):

    def get(self, request):
        return f'Успех GET HomePage'

    def post(self, request):
        return 'Успех POST HomePage'


class DarkPage(View):
    def get(self, request):
        return 'Успех GET DarkPage'

    def post(self, request):
        return 'Успех POST DarkPage'
