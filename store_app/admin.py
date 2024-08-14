from django.contrib import admin

# Register your models here.
from . models import *

class ImagesTublerinlineAdmin(admin.TabularInline):
    model = Images

class TagTublerinlineAdmin(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinlineAdmin,TagTublerinlineAdmin]

class OrderItemTublerinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTublerinline]
    list_display = ['firstname','phone','email','payment_id','date','paid']
    search_fields=['firstname','payment_id','email']

admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact_Us)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
