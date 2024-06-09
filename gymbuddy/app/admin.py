from django.contrib import admin
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import admin, messages
from .models import(Customer,
                    Payment,
                    Notification,
                    Membership_Status,
                    Muscle,
                    SubMuscle,
                    Exercise, 
                    Complaints)
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


def send_renewal_emails(modeladmin, request, queryset):
    today = timezone.now().date()
    expiring_soon = today + timezone.timedelta(days=5)
    memberships = queryset.filter(end_date=expiring_soon, status='active')

    for membership in memberships:
        user = membership.user

        if user.email:
            try:
                send_mail(
                    'Membership Renewal Reminder',
                    f'Dear {user.first_name}, your membership will expire on {membership.end_date}. Please renew your membership to continue enjoying our services.',
                    'bhupinderkaur8284075609@gmail.com', 
                    [user.email],
                    fail_silently=False,
                )
                modeladmin.message_user(request, f"Email sent to {user.email}")
            except Exception as e:
                modeladmin.message_user(request, f"Failed to send email to {user.email}: {e}", level=messages.ERROR)
        else:
            modeladmin.message_user(request, f"User {user.username} does not have an email address.", level=messages.WARNING)

    modeladmin.message_user(request, "Renewal emails sent successfully.", level=messages.SUCCESS)

@admin.register(Membership_Status)
class Membership_Statusmodeladmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date','status' ]
    actions = [send_renewal_emails]

@admin.register(Muscle)
class Musclemodeladmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(SubMuscle)
class SubMusclemodeladmin(admin.ModelAdmin):
    list_display = ['name', 'parent_muscle']

@admin.register(Exercise)
class Exercisemodeladmin(admin.ModelAdmin):
    list_display = ['name', 'sub_muscle']

@admin.register(Complaints)
class Complaintmodeladmin(admin.ModelAdmin):
    list_display = ['user', 'title','description', 'image', 'status']