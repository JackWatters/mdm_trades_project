from django.contrib import admin
from trades.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)


# Register your models here.
