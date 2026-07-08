from django.contrib import admin

from .models import Category, Order, Phone, Review

admin.site.register(Category)
admin.site.register(Phone)
admin.site.register(Review)
admin.site.register(Order)
