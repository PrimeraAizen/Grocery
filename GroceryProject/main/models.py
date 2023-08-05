from django.db import models
from django.urls import reverse



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    category = models.CharField(max_length=100)
    brands = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    reward_points = models.IntegerField()

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    

    # function to return the first 2 sentences of the description
    def short_description(self):
        sentences = self.description.split('.')[0:2]
        return '.'.join(sentences) + '.'