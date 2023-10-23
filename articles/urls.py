from django.conf.urls import url
from . import views

from .views import ArticleEditView

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_details, name="details"),
    url(r'^(?P<slug>[\w-]+)/edit/$', ArticleEditView.as_view(), name="edit"),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.article_delete, name="delete"),
]
