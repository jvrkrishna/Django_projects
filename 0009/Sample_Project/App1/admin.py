from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','created_at')
    list_display_links=('title',)
    list_filter=('created_at','is_published',) #Add to get filters
admin.site.register(Post,PostAdmin)
