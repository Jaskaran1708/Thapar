from django.contrib import admin
from .models import(Customer,
                    Payment,
                    Notification,
                    Membership_Status)
# Register your models here.
@admin.register(Customer)
class Customermodeladmin(admin.ModelAdmin):
    list_display = ['user' , 'email',  'first_name',  'last_name', 'phone_number' , 'join_date' ]

@admin.register(Payment)
class Paymentmodeladmin(admin.ModelAdmin):
    list_display = ['user' ,'amount'  ,'payment_date' ,'payment_method'  ,'status'  ,'renewal_date' ]

@admin.register(Notification)
class Notificationmodeladmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'date','status']

@admin.register(Membership_Status)
class Membership_Statusmodeladmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date','status' ]