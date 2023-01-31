from django.contrib import admin

# Register your models here.

from .models import Blogger, Article, Genre, ArticleInstance
#_______________________________________________________

admin.site.register(Genre)
#_______________________________________________________

class ArticleInline(admin.TabularInline):
    model = Article

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth')
    inlines = [ArticleInline]
#_______________________________________________________

class ArticleInstanceInline(admin.TabularInline):
    model = ArticleInstance

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'issusing_time', 'blogger')
    fieldsets = (
        ('Article',{
            'fields' : ('title','genre')
        }),
        ('Content',{
            'fields' : ('blogger','content')
        }),
    )
    inlines = [ArticleInstanceInline]
#_______________________________________________________

@admin.register(ArticleInstance)
class ArticleInstanceAdmin(admin.ModelAdmin):
    list_filter = ('article','commenter', 'post_time' )
    list_display = ('__str__', 'commenter', 'post_time')