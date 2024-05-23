from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField( max_length=254)
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    phone_number = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='completed')
    renewal_date = models.DateField()

    def __str__(self):
        return str(self.id)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='unread')

    def __str__(self):
        return str(self.id)


class Membership_Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return str(self.id)
