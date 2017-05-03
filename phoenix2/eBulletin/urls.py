from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<login_user_id>[0-9]+)/index/$', views.userindex,name="userindex"),
    url(r'^(?P<login_user_id>[0-9]+)/(?P<bulletin_id>[0-9]+)/list/$', views.message_list,name="message_list"),
    url(r'^login/$', views.userLogin, name="userlogin"),
    url(r'^(?P<login_user_id>[0-9]+)/(?P<message_id>[0-9]+)/detail/$', views.message_detail,name="message_detail"),
    #url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    #url(r'^test/$', views.test),
    #url(r'^(?P<id>[0-9]+)/del/$', views.del_post, name='del_post'),
    #url(r'^(?P<id>[0-9]+)/edit/$$', views.edit_post, name='edit_post')

]