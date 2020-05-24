from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=30) 
    
    def __str__(self):
        return self.title

class QuantityUnit(models.Model):
    unit = models.CharField(max_length=10) 
    
    def __str__(self):
        return self.unit

class IngredientMeta(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  
    
    def __str__(self):
        return self.name

class Receipt(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class ReceiptIngredient(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(IngredientMeta, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.ForeignKey(QuantityUnit, on_delete=models.CASCADE)    
    
    def __str__(self):        
        return '%s: %s' % (self.receipt, self.ingredient)