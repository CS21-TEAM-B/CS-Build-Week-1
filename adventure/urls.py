from django.conf.urls import url
from . import api
# trigger deploy
urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say)
]
