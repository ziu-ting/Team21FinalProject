from django.contrib import admin
from blog import models

class PostAdmin(admin.ModelAdmin):
    list_display=('nickname', 'email', 'title', 'message', 'enabled', 'pub_time')
    ordering=('-pub_time',)
admin.site.register(models.Post, PostAdmin)

