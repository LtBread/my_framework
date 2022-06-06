from framework.url import Url
from views import HomePage, DarkPage

my_urls = [
    Url('/homepage', HomePage),
    Url('/darkpage', DarkPage)
]

