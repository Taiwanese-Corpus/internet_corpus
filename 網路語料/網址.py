# -*- coding: utf-8 -*-
from django.conf.urls import url
from 網路語料.介面 import 全部語料
from 網路語料.介面 import 加語料
from 網路語料.介面 import 看語料
from 網路語料.介面 import 正規化語料


urlpatterns = [
    url(r'^$', 全部語料, name='首頁'),
    url(r'^加$', 加語料, name='加'),
    url(r'^加/(?P<pk>\d+)$', 加語料, name='加'),
    url(r'^正規化/(?P<pk>\d+)$', 正規化語料, name='正規化'),    
    url(r'^看/(?P<pk>\d+)$', 看語料, name='看'),
    url(r'^', 全部語料),
]
