from django.contrib import admin
from FinalProject.common.models import Post


@admin.register(Post)
class PhotoPostAdmin(admin.ModelAdmin):
    pass
