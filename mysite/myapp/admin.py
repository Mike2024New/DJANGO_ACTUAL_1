from django.contrib import admin

from myapp.models import Product

admin.site.register(Product) # регистрация модели для админ панели
