"""
Date: 2019--21 10:15
User: yz
Email: 1147570523@qq.com
Desc:

"""

from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'([0-9]+)/$',views.detail,name='detail')
]