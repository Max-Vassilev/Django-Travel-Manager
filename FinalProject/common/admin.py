from django.contrib import admin
from FinalProject.common.models import Post, Like


@admin.register(Post)
class PhotoPostAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class PostLikeAdmin(admin.ModelAdmin):
    pass
