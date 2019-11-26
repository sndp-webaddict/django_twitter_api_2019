from django.conf.urls import url
from .views import index, callback

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^complete/twitter/$', callback, name='complete_twitter'),
]