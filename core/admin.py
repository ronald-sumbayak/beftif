from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

from core.models import News, Category


class CustomUserAdmin (UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_ ('Personal Info'), {'fields': ('first_name', 'last_name', 'email')}),
    )
    add_fieldsets = [
        (None, {'classes': ['wide', 'extrapretty'], 'fields': ('username', 'password1', 'password2')}),
        (_ ('Personal Info'), {'classes': ['wide', 'extrapretty'], 'fields': ('first_name', 'last_name')}),
    ]
    
    def name (obj):
        return '%s %s' % (obj.first_name, obj.last_name)
    
    list_display = ['username', name]
    list_filter = []
    name.short_description = 'Name'


class NewsAdmin (ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category__name']
    list_per_page = 20
    search_fields = ['title', 'category__name']


admin.site.unregister (User)
admin.site.unregister (Group)
admin.site.register (User, CustomUserAdmin)
admin.site.register (Category)
admin.site.register (News, NewsAdmin)
