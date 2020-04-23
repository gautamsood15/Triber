from django.conf.urls import url

from django.views.generic.base import RedirectView

# from .views import  TweetDetailView, TweetDeleteView, TweetListView, TweetCreateView, TweetUpdateView
from tweets.api.views import TweetListAPIView


urlpatterns = [
#	url(r'^$', RedirectView.as_view(url="/")),
    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'),

]

