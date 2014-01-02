from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.PostListView.as_view(), name="list"),
    url(r"^(?P<pk>\d+)/$", views.PostDetailView.as_view(), name="detail"),
)