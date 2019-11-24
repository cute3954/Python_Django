from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    # ログイン
    path(r'^accounts/login/$', LoginView.as_view(), name='login'),
    # ログアウト
    path(r'^accounts/logout/$', LogoutView.as_view(), name='logout', kwargs={'next_page' : '/'}),
    path('', views.post_list, name='post_list'),
    path(r'^post/<int:pk>/', views.post_detail, name='post_detail'),
    path(r'^post/new', views.post_new, name='post_new'),
    # 一時保存
    path(r'^draft/$', views.post_draft_list, name='post_draft_list'),
    # 書き込みアップ
    path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    # 書き込み修正
    path(r'^post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 書き込み削除
    path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # コメント追加
    path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name="add_comment_to_post"),
    # コメント承認
    path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name="comment_approve"),
    # コメント削除
    path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name="comment_remove"),
]
