from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
        list_display = ["post_title",
                        # "post_content",
                        "is_active",
                        "sort_order",
                        "is_publicated",
                        "created",
                        "updated"]
        # list_display = [field.name for field in Post._meta.fields] #show all fields

admin.site.register(Post, PostAdmin)
