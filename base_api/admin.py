from django.contrib import admin
from .models import Author , Customer , Book , Order

# Register your models here.
admin.site.register(Author)
admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)