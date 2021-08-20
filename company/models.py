from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    
    product_id = models.IntegerField( primary_key=True)
    brand = models.TextField()
    product_name = models.TextField()
    date = models.DateField( default=datetime.utcnow)
    description =  models.TextField()
    category =  models.TextField()
    price = models.FloatField( )
    condition = models.TextField()
    # image = models.TextField()
    delivery_available = models.BooleanField(default=False)
    discount = models.FloatField( default=0.0)
    product_count = models.IntegerField(default=1)
    def __str__(self):
       return self.product_name
    

class WishList(models.Model):

    product_id = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, primary_key=True)
    product_name = models.ManyToManyField(Product)
    date = models.DateField(default=datetime.utcnow)
    # product = models.FilteredRelation('Product', back_populates='wishlists')
    def __str__(self):
       return str(self.product_id)