from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    fields = ("published", "title", "slug", "content", "author")
    list_display = ["published", "title", "updated_at"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated_at", "author"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)
