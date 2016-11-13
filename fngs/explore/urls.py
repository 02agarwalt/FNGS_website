from django.conf.urls import url
from . import views


app_name = 'explore'

urlpatterns = [
	# /explore/
    url(r'^$', views.index, name='index'),
    # /explore/<dataset_id>/
    url(r'^(?P<dataset_id>[\w\-]+)/$', views.dataset, name='dataset'),
]
