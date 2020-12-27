from django.db import models

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = ("list")
        verbose_name_plural = ("lists")

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    list_host = models.ForeignKey(List, on_delete=models.CASCADE)
    date_limit = models.DateField(auto_now=False, auto_now_add=False, default=None, blank=True, null=True)

    class Meta:
        verbose_name = ("item")
        verbose_name_plural = ("items")
    
    def __str__(self):
        return self.name
