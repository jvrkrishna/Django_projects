from django.contrib import admin
from .models import Post,Sample
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','created_at')
    list_display_links=('title',)
    list_filter=('created_at','author',) #Add to get filters
admin.site.register(Post,PostAdmin)
admin.site.register(Sample,PostAdmin)