from django.conf.urls import url

from django.views.generic.base import RedirectView

# from .views import  TweetDetailView, TweetDeleteView, TweetListView, TweetCreateView, TweetUpdateView
from .views import LikeToggleAPIView,RetweetAPIView,TweetCreateAPIView,TweetListAPIView


urlpatterns = [
#	url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', TweetListAPIView.as_view(), name='list'),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),
#   url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
#   url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
#   url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]

