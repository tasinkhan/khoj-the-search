from django.contrib import admin
from .models import Search

# Register your models here.

app_name='Search'

class SearchAdmin(admin.ModelAdmin):
    list_display=('user','input_values','timestamp')

admin.site.register(Search, SearchAdmin)