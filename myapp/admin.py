from django.contrib import admin

# Register your models here


from .models import Register, Join

admin.site.register(Register)
admin.site.register(Join)