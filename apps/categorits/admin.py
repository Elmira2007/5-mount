from django.contrib import admin

from apps.categorits.models import Categorits

# Register your models here.
@admin.register(Categorits)
class CategoritsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title', )}