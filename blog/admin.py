from django.contrib import admin

# Register your models here.
from blog.models import blog,Comment
class CommentInline(admin.StackedInline): 
    model = Comment
    extra = 0
class blogAdmin(admin.ModelAdmin):
    inlines =[ 
             CommentInline,
             ]
admin.site.register(blog,blogAdmin)
admin.site.register(Comment)