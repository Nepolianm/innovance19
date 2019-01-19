from django.db import models


# Create your models here.
class Registration(models.Model):
    choices = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    mob = models.CharField(max_length=20)
    is_veg = models.BooleanField(default=True)
    accommodation = models.BooleanField(default=True)
    is_ieee_member = models.BooleanField(default=True)
    member_id = models.CharField(max_length=100, null=True, blank=True)
    college = models.CharField(max_length=100)
    t_shirt_size = models.CharField(max_length=1, choices=choices)
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    is_paid = models.BooleanField(default=True)
