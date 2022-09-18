from django.contrib import admin
from .models import*

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','toto','prev_price','price','alcaholic','created','updated','digital','status')
	list_filter = ('status','created')
	search_fields = ('name',)
	date_hierarchy = 'created'
	ordering = ('name',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
	list_display = ('user','product','value')
	list_filter = ('product',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name','PhoneNumber','email','date_created')
	list_filter = ('name',)
	search_fields = ('date_created',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('customer','date_ordered','status','transactions_id')
	list_filter = ('date_ordered',)
	search_fields = ('customer',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('product', 'order','quantity','date_added')
	list_filter = ('date_added',)
	search_fields = ('product','date_added','quantity')

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
	list_display = ('customer', 'order','address','city','phone','date_added')
	list_filter = ('city','address','date_added')
	search_fields = ('address','city','order','date_added')

@admin.register(Regionz)
class RegionzAdmin(admin.ModelAdmin):
	list_display = ('rname','date_added')
	search_fields = ('rname',)


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
	list_display = ('region','town_name','address')
	search_fields = ('town_name',)