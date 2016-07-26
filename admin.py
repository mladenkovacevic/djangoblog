from django.contrib import admin
from .models import Post


### Admin
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    fields = ("published", "title", "slug", "body", "author")
    list_display = ["published", "title", "updated"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated", "author"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "body"]

admin.site.register(Post, PostAdmin)
