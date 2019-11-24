from django.contrib import admin
from .models import Post, Comment

# 管理者パネルにモデルを登録する
admin.site.register(Post)
admin.site.register(Comment)
