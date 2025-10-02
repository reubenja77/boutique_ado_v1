from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0

class Orderadmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)

    readonly_fields = ('order_number', 'date', 
                       'delivery_cost', 'order_total', 
                       'grand_total')

    fields = ('order_number', 'full_name', 'email', 'phone_number',
              'country', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'date',
              'delivery_cost', 'order_total', 'grand_total')

    list_display = ('order_number', 'date', 'full_name', 
                    'order_total', 'delivery_cost', 
                    'grand_total')

    ordering = ('-date',)

admin.site.register(Order, Orderadmin)