from framework.url import Url
from views import DefaultPage, HomePage, DarkPage

my_urls = [
    Url('/', DefaultPage),
    Url('/homepage', HomePage),
    Url('/darkpage', DarkPage)
]

