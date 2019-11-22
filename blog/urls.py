from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    # 一時保存
    path(r'^draft/$', views.post_draft_list, name='post_draft_list'),
    # 書き込みアップ
    path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    # 書き込み修正
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 書き込み削除
    path(r'^post/(?p\P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
