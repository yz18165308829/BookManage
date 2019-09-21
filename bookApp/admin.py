from django.contrib import admin

# Register your models here.
from .models import Book,Hero

# class HeroINline(admin.TabularInline):
class HeroINline(admin.StackedInline):
    model = Hero
    extra = 2

class BookAdmin(admin.ModelAdmin):
   list_display = ['pk', 'title', 'pub_date']
   list_filter = ['title']
   search_fields = ['title']
   list_per_page = 10
   inlines = [HeroINline]
   # fields = ['pub_date', 'title']
   fieldsets = [('基础信息', {'fields': ['title']}),
                ('详细信息', {'fields': ['pub_date']}), ]
# 人物自定义管理页面
class HeroAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'sex', 'content']
   list_filter = ['name']
   search_fields = ['name']
   list_per_page = 10
   fieldsets = [('基础信息', {'fields': ['name','gender']}),
                ('详细信息', {'fields': ['content']}), ]

admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)
