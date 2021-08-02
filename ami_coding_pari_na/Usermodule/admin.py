from django.contrib import admin
from .models import CustomUser
# Register your models here.
app_name='Usermodule'
admin.site.register(CustomUser)