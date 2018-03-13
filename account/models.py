from django.db import models

# Create your models here.
class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Will implement default name with 
    name = models.CharField(max_length=100, blank=False, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    accountType = models.CharField(max_length=24, blank=True, null=True)
    
    class Meta:
        ordering = ('created','name')

