from django.contrib import admin

# Register your models here.
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title',) # show title in list view
    fields= ('title','content')# Fields to show in the edit  form

admin.site.register(BlogPost,BlogPostAdmin)